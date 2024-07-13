import time

from utils.logger import Logger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserInvestments(APIView):
	''' This API is used to fetch Investments details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Investments data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class UserSavings(APIView):
	''' This API is used to fetch savings details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Savings data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class UserExpences(APIView):
	''' This API is used to fetch expenses details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Expences data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class DownloadExcel(APIView):
	''' This API is used to download finance data '''
	def post(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Expences data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)

