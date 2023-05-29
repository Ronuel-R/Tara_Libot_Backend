from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response
from tara_libot_web_client.models.models import Account
############ CONSTANTS ##################
from constants.login_helper import LoginHelper
from constants.http_messages import *
import jwt
import datetime

class LoginAdminView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        serializer = LoginAdminSerializer(data=request.data)

        if not serializer.is_valid():
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": serializer.errors})

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        errors = LoginHelper.validate_email_and_password(self,email, password)

        if len(errors) != 0:
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        user = LoginHelper.authenticate_user(self, email, password)

        if user:
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=240),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            data['JWT'] = token
            response = Response()
            response.set_cookie(key='JWT', value=token, httponly=True,  samesite='None', secure=True)
            response.data = {
            'status' : ok,
            'message': 'Login Successfully',
            "data": data,
            "errors": errors
        }
            return response

        else:

            message = 'User not authenticated'
            status = unauthorized
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
