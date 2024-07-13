from datetime import datetime

from utils.logger import Logger
from utils.connectors import Connections
from utils.secureText import SecureText
from utils.models import AuthUser
from utils.validators import UserLoginValidator, RegisterUserValidator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from pydantic import ValidationError as PydanticValidationError


class UserLogin(TokenObtainPairView):
	def post(self, request, format=None):
		''' This API is used to authenticate user '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			# Validate request data
			UserLoginValidator(username=username, password=password)
			# Manipulatig request object
			_mutable = request.POST._mutable
			request.POST._mutable = True
			request.POST['username'] = SecureText._ref._encryptText(username)
			request.POST['password'] = password
			request.POST._mutable = _mutable
			# user authentication
			res = super().post(request)
			DATA = res.data
			if 'access' in DATA and 'refresh' in DATA:
				API_STATUS  = status.HTTP_200_OK
				API_MESSAGE = 'User authentication successful!'
		except TypeError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except PydanticValidationError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except ValidationError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except AuthenticationFailed as exc:
			Logger._ref._logException(exc)
			API_STATUS  = status.HTTP_401_UNAUTHORIZED
			API_MESSAGE = str(exc)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class RegisterUser(APIView):
	''' This API is used to register a new user '''
	def post(self, request, format=None):
		API_PROCESSING_TIME = datetime.now()
		API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			firstName = request.POST.get('firstName')
			lastName  = request.POST.get('lastName')
			username  = request.POST.get('username')
			email 	  = request.POST.get('email')
			password  = request.POST.get('password')
			userId 	  = request.POST.get('userId', 1)
			# Validate request data
			RegisterUserValidator.model_construct(firstName=firstName, lastName=lastName, username=username, email=email, password=password, userId=userId)
			# get postgres conn
			session = Connections.getPostgresConnection()
			# new user data
			userData = AuthUser(
				first_name = firstName,
				last_name  = lastName,
				email 	   = SecureText._ref._encryptText(email),
				username   = SecureText._ref._encryptText(username),
				password   = make_password(password),
				created_by = userId
			)
			# Save the user data in the database
			session.add(userData)
			session.commit()
			# update respone
			API_STATUS  = status.HTTP_201_CREATED
			API_MESSAGE = 'User registration successful!'
			DATA = { 'userId': userData.id }
			# close session
			session.close()
		except TypeError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except PydanticValidationError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except ValidationError as exc:
			Logger._ref._logError(exc)
			API_STATUS  = status.HTTP_400_BAD_REQUEST
			API_MESSAGE = str(exc)
		except Exception as exc:
			Logger._ref._logError(exc)
		 # calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'   : DATA
		}, status=API_STATUS)


class UpdateUserDetails(APIView):
	def post(self, request, format=None):
		''' This API is used to update user details [post login] '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'User data updated successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'   : DATA
		}, status=API_STATUS)


class ForgotPassword(APIView):
	def post(self, request, format=None):
		''' This API is used to update user details [reset login pass] '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Password updated successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class DeleteUser(APIView):
	def post(self, request, format=None):
		''' This API is used to delete user account '''
		API_PROCESSING_TIME = datetime.now()
		API_STATUS  = status.HTTP_500_INTERNAL_SERVER_ERROR
		API_MESSAGE = 'Something went wrong! Please try after sometime!'
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'User account deleted successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)

