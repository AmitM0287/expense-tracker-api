import os
import tempfile
from datetime import datetime
from library.loggers.logger import Logger
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from langdetect import detect
from gtts import gTTS
from django.http import FileResponse
from googletrans import Translator


class TextToSpeech(APIView):
	def post(self, request, format=None):
		''' This API downloads and optionally converts YouTube videos '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = ''
		DATA = {}
		resType = 'data'

		text = request.POST.get("text")
		output_lang = request.POST.get("output_lang", "en")
		lang = detect(text)

		if not text:
			API_STATUS = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = "The 'text' field is required."

		if lang not in ["en", "bn"]:
			API_STATUS = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = {"error": "Supported languages are 'en' (English) and 'bn' (Bengali)."}
		
		try:
			# Translate English to Bengali if requested
			translated_text = text
			if lang == "en" and output_lang == "bn":
				translator = Translator()
				translated_text = translator.translate(text, src=lang, dest=output_lang).text
			# Generate speech
			tts = gTTS(text=translated_text, lang=output_lang)
			
			# Use a temporary file to save the audio
			with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
				tts.save(temp_file.name)
				temp_file_name = temp_file.name

			# Return the audio file
			response = FileResponse(open(temp_file_name, "rb"), content_type="audio/mpeg")
			response["Content-Disposition"] = f"attachment; filename=output.mp3"
			
			# Clean up the temporary file
			os.unlink(temp_file_name)
			return response

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
			resType: DATA
		}, status=API_STATUS)

