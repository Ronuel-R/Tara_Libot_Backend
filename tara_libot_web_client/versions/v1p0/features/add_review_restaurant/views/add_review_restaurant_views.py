from ......models.models import Comments, Business, Account
from rest_framework.views import APIView
import pytz
from rest_framework.response import Response
from django.utils import timezone
from ..serializers.reviews_serializers import ReviewSerializers
from constants.http_messages import *
from django.http import Http404 
from constants.auth_user import AuthUser

from rest_framework.response import Response

import pytz

class AddReview(APIView):
    def get_restaurant(self, pk, format=None):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        business = self.get_restaurant(pk)
        serializer = ReviewSerializers(context={'view': self}, data=request.data)

        if serializer.is_valid():
                user= Account.objects.filter(id = payload['id']).first()
                
                phil_tz = pytz.timezone('Asia/Manila')

                comments = Comments.objects.create(
                    content=request.data['content'],
                    business=business,
                    rating=request.data['rating'],
                    created_at=timezone.now().astimezone(phil_tz),
                    created_by = user,
                    likes=0
                )

            

                data = serializer.data
                data['created_by'] = {
                'id': user.id,
                'user': {
                    
                    'username': user.user.username,
                    'email': user.user.email,
                    
                }
            }

                errors = {}
                status = created
                message = 'Success'

                return Response({"message": message, "data": data, "status": status, "errors": errors})
            
        else:
            data = {}
            message = 'Ehhhhhhh'
            errors = serializer.errors
            status = bad_request
        
            return Response({"message": message, "data": data, "status": status, "errors": errors})

