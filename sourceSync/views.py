import time
import os

from utils.logger import Logger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load env
load_dotenv()


class SyncGoogleSheet(APIView):
	def post(self, request, format=None):
		''' This API is used to synced data with google sheets '''
		API_PROCESSING_TIME = time.time()
		API_STATUS  = None
		API_MESSAGE = ''
		DATA = {}
		try:
			# The id and range of the spreadsheet
			spreadsheetId = request.POST.get('spreadsheetId')
			spreadsheetRange = request.POST.get('spreadsheetRange')
			# Path to the service account key file
			SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
			SCOPES = os.getenv('SCOPES').split(',')
			# Load the Google Sheets API credentials
			credentials = service_account.Credentials.from_service_account_file(
				filename = SERVICE_ACCOUNT_FILE, 
				scopes	 = SCOPES
			)
			# Build the service
			service = build('sheets', 'v4', credentials=credentials)
			# Call the Sheets API
			sheet = service.spreadsheets()
			result = sheet.values().get(spreadsheetId=spreadsheetId, range=spreadsheetRange).execute()
			# Update response
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Synced with google sheet successfully!'
			DATA = result.get('values', [])
		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)
			API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		# Calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# Log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		# Return response
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)

