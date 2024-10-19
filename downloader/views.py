from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import FileResponse
from library.loggers.logger import Logger
from datetime import datetime
import subprocess
import os
from django.conf import settings
import re


class YouTubeDownloader(APIView):
    def post(self, request, format=None):
        ''' This API is used to download YouTube videos, shorts '''
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = ''
        DATA = {}

        try:
            video_url = request.POST.get('url')
            if not video_url:
                API_STATUS = status.HTTP_400_BAD_REQUEST
                raise Exception('No URL provided!')

            # Set the output file name format
            output_file_name = os.path.join(settings.MEDIA_ROOT, '%(id)s.%(ext)s')  
            command = f'yt-dlp -o "{output_file_name}" "{video_url}"'

            # Execute the yt-dlp command
            subprocess.run(command, shell=True, check=True)
            print("Downloaded video.")

            # Generate the downloaded file path
            video_id = self.extract_video_id(video_url)
            if not video_id:
                raise Exception("Could not extract video ID from the URL.")
            
            downloaded_file_path = os.path.join(settings.MEDIA_ROOT, f'{video_id}.webm')

            # Return the file as a stream
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
        # Regex patterns to match video IDs in various URL formats
        patterns = [
            r'(?<=v=)[\w-]{11}',  # For standard URLs: https://www.youtube.com/watch?v=VIDEO_ID
            r'(?<=youtu\.be/)[\w-]{11}',  # For shortened URLs: https://youtu.be/VIDEO_ID
            r'(?<=shorts/)[\w-]{11}'  # For Shorts URLs: https://www.youtube.com/shorts/VIDEO_ID
        ]

        for pattern in patterns:
            match = re.search(pattern, video_url)
            if match:
                return match.group(0)  # Return the matched video ID
        
        return None  # If no video ID is found
