from rest_framework.views import APIView
from rest_framework.response import Response

import jwt
############ CONSTANTS ##################

from constants.http_messages import *

class LogoutAdminView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        token = request.COOKIES.get('jwt')

        if not token:
            errors = 'Invalid token'
            status = bad_request
            message = 'You are not logged in'
            return Response({"status": status, "message": message, "data": data, "errors": errors})

        try:
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'status' : ok,
                'Message': 'Logout Successfully',
                'data' : data,
                'errors' : errors 
            }
            return response
        
        except Exception as e:
            message = 'Internal server error'
            status_code = internal_server_error
            return Response({"status": status_code, "message": message, "data": data, "errors": errors})