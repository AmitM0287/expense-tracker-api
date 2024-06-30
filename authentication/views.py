from datetime import datetime
from expenseTracker.logger import Logger
from expenseTracker.connections import Connections
from expenseTracker.secureText import SecureText
from expenseTracker.models import AuthUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password


class UserLogin(TokenObtainPairView):
    ''' This is used to authenticate user '''
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = 'Something went wrong! Please try after sometime!'
        DATA = {}
        try:
            # process the user authentication
            res = super().post(request)
            DATA = res.data
            if 'access' in DATA and 'refresh' in DATA:
                API_STATUS = status.HTTP_200_OK
                API_MESSAGE = 'User authentication successful!'
        except AuthenticationFailed as exc:
            Logger._ref._logException(exc)
            API_STATUS = status.HTTP_401_UNAUTHORIZED
            API_MESSAGE = str(exc)
        except Exception as exc:
            Logger._ref._logError(exc)
        # calculate the processing time in milliseconds
        API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
        # log the processing time, message, and status
        Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
        return Response({
            'processingTime': API_PROCESSING_TIME,
            'status': API_STATUS,
            'message': API_MESSAGE,
            'data': DATA
        }, status=API_STATUS)


class UserRegister(APIView):
    ''' This is used to register a new user '''
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = 'Something went wrong! Please try after sometime!'
        DATA = {}
        try:
            # get postgres conn
            session = Connections.getPostgresConnection()
            # new user data
            userData = AuthUser(
                first_name = 'yyy',
                last_name = 'yyy',
                email = SecureText._ref._encryptText('yyy@yyy.yy'),
                username = SecureText._ref._encryptText('yyy@yyy.yy'),
                password = make_password('yyyyy@yyyyy'),
                created_by = 1
            )
            # Save the user data in the database
            session.add(userData)
            session.commit()
            session.close()
            # update respone
            API_STATUS = status.HTTP_201_CREATED
            API_MESSAGE = 'User registration successful!'
        except Exception as exc:
            Logger._ref._logError(exc)
         # calculate the processing time in milliseconds
        API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
        # log the processing time, message, and status
        Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
        return Response({
            'processingTime': API_PROCESSING_TIME,
            'status': API_STATUS,
            'message': API_MESSAGE,
            'data': DATA
        }, status=API_STATUS)


class UpdateUser(APIView):
    def get(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = 'Something went wrong! Please try after sometime!'
        DATA = {}
        try:
            API_STATUS = status.HTTP_200_OK
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
            'status': API_STATUS,
            'message': API_MESSAGE,
            'data': DATA
        }, status=API_STATUS)


class ForgotPassword(APIView):
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = 'Something went wrong! Please try after sometime!'
        DATA = {}
        try:
            API_STATUS = status.HTTP_200_OK
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
            'status': API_STATUS,
            'message': API_MESSAGE,
            'data': DATA
        }, status=API_STATUS)


class DeleteUser(APIView):
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
        API_MESSAGE = 'Something went wrong! Please try after sometime!'
        DATA = {}
        try:
            API_STATUS = status.HTTP_200_OK
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
            'status': API_STATUS,
            'message': API_MESSAGE,
            'data': DATA
        }, status=API_STATUS)

