from expenseTracker.logger import logger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from datetime import datetime
from expenseTracker.connections import getPostgresConnection
from expenseTracker.models import AuthUser
from django.contrib.auth.hashers import make_password

class UserLogin(TokenObtainPairView):
    ''' This is used to authenticate user '''
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_MESSAGE = None
        API_STATUS = None
        DATA = {}
        try:
            # Process the user authentication
            res = super().post(request)
            DATA = res.data
            logger.info('User authentication successful.')
        except Exception as exc:
            # Log any exceptions that occur during authentication
            logger.error(f'User authentication error: {exc}')
        # Calculate the processing time in milliseconds
        API_PROCESSING_TIME = int((datetime.now() - API_PROCESSING_TIME).total_seconds() * 1000)
        # Log the processing time, message, and status
        logger.info(f'Processing time: {API_PROCESSING_TIME} ms | Message: {API_MESSAGE} | Status: {API_STATUS}')
        return Response({
            'processingTime': API_PROCESSING_TIME,
            'message': API_MESSAGE,
            'status': API_STATUS,
            'data': DATA
        }, status=API_STATUS)

class UserRegister(APIView):
    ''' This is used to register a new user '''
    def post(self, request):
        API_PROCESSING_TIME = datetime.now()
        API_MESSAGE = None
        API_STATUS = None
        DATA = {}
        # get postgres conn
        session = getPostgresConnection()
        userData = AuthUser(
            first_name = 'yyy',
            last_name = 'yyy',
            email = 'yyy@yyy.yy',
            username = 'yyy@yyy.yy',
            password = make_password('yyyyy@yyyyy'),
            created_by = 1
        )
        # Save the user data in the database
        session.add(userData)
        session.commit()
        session.close()
        # Return response
        return Response({
            'processingTime': API_PROCESSING_TIME,
            'message': API_MESSAGE,
            'status': API_STATUS,
            'data': DATA
        }, status=API_STATUS)
