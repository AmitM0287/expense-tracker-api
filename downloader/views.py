import subprocess
import zipfile
import shutil
import subprocess
import os
import re
import time
from datetime import datetime

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import StreamingHttpResponse, FileResponse
from library.loggers.logger import Logger
from django.conf import settings


class YouTubeDownloader(APIView):
	permission_classes = [AllowAny]
	authentication_classes = []

	def post(self, request, format=None):
		''' This API downloads and optionally converts YouTube videos '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = ''
		DATA = {}

		try:
			# Get the video URL and target format from the request
			video_url = request.POST.get('url', 'https://youtube.com/shorts/JBiEPm48H-I?feature=shared')
			target_format = request.POST.get('format', 'mp4')  # Default to mp4 if not specified

			if not video_url:
				API_STATUS = status.HTTP_400_BAD_REQUEST
				raise Exception('No URL provided!')

			# Define output file name for yt-dlp
			output_file_name = os.path.join(settings.MEDIA_ROOT, '%(id)s.%(ext)s')
			command = f'yt-dlp -o "{output_file_name}" "{video_url}"'
			subprocess.run(command, shell=True, check=True)
			print("Downloaded video.")

			# Extract video ID from the provided URL
			video_id = self.extract_video_id(video_url)
			if not video_id:
				raise Exception("Could not extract video ID from the URL.")
			
			# Path to the downloaded file
			downloaded_file_path = os.path.join(settings.MEDIA_ROOT, f'{video_id}.webm')

			# Convert the video to the specified format if needed
			if target_format in ['mp4', 'mov']:
				return self.convert_video_format_with_progress(downloaded_file_path, target_format)
			else:
				# If no conversion is needed, return the original file
				response = FileResponse(open(downloaded_file_path, 'rb'))
				response['Content-Disposition'] = f'attachment; filename="{os.path.basename(downloaded_file_path)}"'
				return response

		except subprocess.CalledProcessError as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)

		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)

		# Calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# Log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)

		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status': API_STATUS,
			'message': API_MESSAGE,
			'data': DATA
		}, status=API_STATUS)

	def extract_video_id(self, video_url):
		'''
		Extract video ID from various YouTube URL formats.
		Supports regular video URLs and Shorts URLs.
		'''
		patterns = [
			r'(?<=v=)[\w-]{11}',  # Standard URLs: https://www.youtube.com/watch?v=VIDEO_ID
			r'(?<=youtu\.be/)[\w-]{11}',  # Shortened URLs: https://youtu.be/VIDEO_ID
			r'(?<=shorts/)[\w-]{11}'  # Shorts URLs: https://www.youtube.com/shorts/VIDEO_ID
		]

		for pattern in patterns:
			match = re.search(pattern, video_url)
			if match:
				return match.group(0)  # Return the matched video ID
		
		return None  # Return None if no video ID is found

	def convert_video_format_with_progress(self, input_file, target_format):
		'''
		Converts the downloaded .webm file to the specified format (mp4 or mov),
		with real-time progress tracking using StreamingHttpResponse.
		'''
		# Define output file name based on target format
		output_file_name = os.path.splitext(os.path.basename(input_file))[0] + f'.{target_format}'
		output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)

		# ffmpeg command for conversion
		command = [
			'ffmpeg', '-i', input_file,
			'-c:v', 'libx264', '-crf', '20', '-preset', 'fast',
			'-c:a', 'aac', '-b:a', '192k',
			output_file_path
		]

		# Get the total duration of the video for progress calculation
		total_duration_cmd = [
			'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
			'-of', 'default=noprint_wrappers=1:nokey=1', input_file
		]
		total_duration = float(subprocess.check_output(total_duration_cmd).strip())

		# Generator function to yield progress updates
		def generate_progress():
			process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)
			time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')

			for line in process.stderr:
				match = time_pattern.search(line)
				if match:
					current_time_str = match.group(1)
					h, m, s = map(float, current_time_str.split(':'))
					current_time = h * 3600 + m * 60 + s

					# Calculate progress as a percentage
					progress = (current_time / total_duration) * 100
					yield f"data: {{\"progress\": {progress:.2f}}}\n\n"
					time.sleep(0.5)  # Slight delay to control frequency of updates

			process.communicate()  # Wait for the process to finish
			yield f"data: {{\"progress\": 100}}\n\n"  # Complete progress
			os.remove(input_file)  # Remove the original downloaded file after conversion

		return StreamingHttpResponse(generate_progress(), content_type="text/event-stream")


class VideoSplitter(APIView):
	def post(self, request, format=None):
		''' This API splits a video file into parts based on specified time duration and compresses the output into a zip file. '''
		API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = ''
		DATA = {}

		try:
			# Get the uploaded file
			video_file = request.FILES.get('file')  
			split_time = request.data.get('split_time')  # Time to split in seconds

			# Validate the uploaded file
			if not video_file or not video_file.name.endswith(('.mp4', '.mov')):
				API_STATUS = status.HTTP_400_BAD_REQUEST
				raise Exception('Please upload a valid .mp4 or .mov file.')

			# Validate the split time input
			if not split_time or not split_time.isdigit():
				API_STATUS = status.HTTP_400_BAD_REQUEST
				raise Exception('Please provide a valid split time in seconds.')

			split_time = int(split_time)  # Convert split time to integer

			# Define the directory to save the uploaded video
			folder_name = os.path.splitext(video_file.name)[0]
			video_upload_path = os.path.join(settings.MEDIA_ROOT, folder_name)
			os.makedirs(video_upload_path, exist_ok=True)  # Create directory if it doesn't exist

			# Save the uploaded file to the specified directory
			file_path = os.path.join(video_upload_path, video_file.name)
			with open(file_path, 'wb+') as destination:
				for chunk in video_file.chunks():
					destination.write(chunk)

			# Split the video using ffmpeg
			output_files = self.split_video(file_path, split_time)

			# Create a zip file of the output files
			zip_file_path = self.create_zip_file(video_upload_path, folder_name)

			# Clean up the split files and the uploaded folder after zipping
			self.cleanup_files(output_files, video_upload_path)

			# Return the generated zip file path
			DATA = {"zip_file": zip_file_path}
			API_STATUS = status.HTTP_200_OK
			API_MESSAGE = 'Video split and zipped successfully.'

		except Exception as exc:
			API_MESSAGE = str(exc)

		return Response({
			'status': API_STATUS,
			'message': API_MESSAGE,
			'data': DATA
		}, status=API_STATUS)

	def split_video(self, input_file, split_time):
		''' Split the video into parts of specified duration using ffmpeg. '''
		output_files = []
		base_name = os.path.splitext(os.path.basename(input_file))[0]
		output_dir = os.path.dirname(input_file)  # Use the same directory as the input file
		
		# Get the total duration of the video in seconds using ffprobe
		duration_cmd = [
			'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
			'-of', 'default=noprint_wrappers=1:nokey=1', input_file
		]
		total_duration = float(subprocess.check_output(duration_cmd).strip())
		
		# Calculate the number of full segments and the remaining duration
		num_segments = int(total_duration // split_time)
		remaining_time = total_duration % split_time

		# Create full segments
		for i in range(num_segments):
			start_time = i * split_time
			output_file_path = os.path.join(output_dir, f'{base_name}_{i + 1}.mov')
			output_files.append(output_file_path)

			# Construct the ffmpeg command to create each segment
			command = [
				'ffmpeg', '-ss', str(start_time),  # Start time for each segment
				'-i', input_file,
				'-c', 'copy',  # Copy streams without re-encoding
				'-t', str(split_time),  # Duration of the segment
				output_file_path
			]
			
			# Run the ffmpeg command
			subprocess.run(command, check=True)

		# Handle the remaining time if it's greater than zero
		if remaining_time > 0:
			start_time = num_segments * split_time
			output_file_path = os.path.join(output_dir, f'{base_name}_{num_segments + 1}.mov')
			output_files.append(output_file_path)

			# Construct the ffmpeg command for the remaining segment
			command = [
				'ffmpeg', '-ss', str(start_time),  # Start time for the remaining segment
				'-i', input_file,
				'-c', 'copy',  # Copy streams without re-encoding
				'-t', str(remaining_time),  # Duration of the remaining segment
				output_file_path
			]
			
			# Run the ffmpeg command
			subprocess.run(command, check=True)

		return output_files

	def create_zip_file(self, directory, folder_name):
		''' Create a zip file containing all files in the specified directory. '''
		zip_file_path = os.path.join(settings.MEDIA_ROOT, f'{folder_name}.zip')
		
		with zipfile.ZipFile(zip_file_path, 'w') as zipf:
			for root, _, files in os.walk(directory):
				for file in files:
					# Avoid adding the zip file itself to the zip
					if file == f'{folder_name}.zip':
						continue
					file_path = os.path.join(root, file)
					zipf.write(file_path, os.path.relpath(file_path, directory))
		
		return zip_file_path

	def cleanup_files(self, output_files, folder_path):
		''' Remove the split files and the uploaded folder after zipping. '''
		for file in output_files:
			if os.path.exists(file):
				os.remove(file)
		# Remove the folder containing the uploaded file
		if os.path.exists(folder_path):
			shutil.rmtree(folder_path)  # Remove the directory and all its contents


class MediaCleanupView(APIView):
    def post(self, request, format=None):
        ''' Cleans up media files based on provided criteria. '''
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = ''
        DATA = {'cleaned_files': [], 'errors': []}

        # Path to the media folder
        media_dir = settings.MEDIA_ROOT  # Ensure MEDIA_ROOT is defined in your settings

        # Get the default time if defined in settings, in minutes
        default_time = getattr(settings, 'DEFAULT_CLEANUP_TIME', 30)  # Default to 30 minutes if not set
        thirty_minutes_ago = time.time() - (default_time * 60)  # Convert minutes to seconds

        # Get the filename from the request data
        filename_to_delete = request.data.get('filename', None)

        try:
            if filename_to_delete:
                # If a filename is provided, attempt to delete it
                file_path = os.path.join(media_dir, filename_to_delete)

                if os.path.isfile(file_path):
                    os.unlink(file_path)  # Delete the specified file
                    DATA['cleaned_files'].append(filename_to_delete)
                    API_MESSAGE = f'Deleted: {filename_to_delete}.'
                else:
                    API_MESSAGE = f'File not found: {filename_to_delete}.'

            else:
                # If no filename provided, delete files older than default_time
                for filename in os.listdir(media_dir):
                    file_path = os.path.join(media_dir, filename)

                    # Check if it is a file and exists
                    if os.path.isfile(file_path):
                        # Get the last modified time
                        file_mod_time = os.path.getmtime(file_path)

                        # Check if the file is older than the specified time
                        if file_mod_time < thirty_minutes_ago:
                            os.unlink(file_path)  # Delete the file
                            DATA['cleaned_files'].append(filename)

                API_MESSAGE = f'Cleaned up {len(DATA["cleaned_files"])} files older than {default_time} minutes.'

            API_STATUS = status.HTTP_200_OK

            # Calculate the processing time in milliseconds
            API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)

            # Log the processing time, message, and status
            Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
            
            return Response({
                'processingTime': API_PROCESSING_TIME,
                'status': API_STATUS,
                'message': API_MESSAGE,
                'data': DATA
            }, status=API_STATUS)

        except Exception as e:
            Logger._ref._logError(f"Error during cleanup: {str(e)}")
            return Response({
                'status': 'error',
                'message': f'An error occurred: {str(e)}',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

