from rest_framework.views import APIView
from tara_libot_web_client.models.models import FoodComments , Foods, Account
from constants.auth_user import AuthUser
from constants.http_messages import *
from rest_framework.response import Response
from ..serializers.food_review_serializers import FoodReviewSerializers
from django.http import Http404
import pytz
from django.utils import timezone 

class AddFoodReview(APIView):   
    
    def get_food(self, pk, format=None):
            try:
                return Foods.objects.get(pk=pk)
            except Foods.DoesNotExist:
                raise Http404

    def post(self, request, pk, format=None):
            token = AuthUser.get_token(request)

            if type(token) == dict:
                return Response(token)

            payload = AuthUser.get_user(token)

            if 'errors' in payload:
                return Response(payload)

            food = self.get_food(pk)
            
            serializer = FoodReviewSerializers(context={'view': self}, data=request.data)

            if serializer.is_valid():
                    user= Account.objects.filter(id = payload['id']).first()
                    
                    phil_tz = pytz.timezone('Asia/Manila')

                    food_comments = FoodComments.objects.create(
                        content=request.data['content'],
                        food=food,
                        rating=request.data['rating'],
                        created_at=timezone.now().astimezone(phil_tz),
                        created_by = user,
                        
                    )
                    food_comments.likes.set([])

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