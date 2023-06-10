from rest_framework.response import Response
from rest_framework.views import APIView
from constants.auth_user import AuthUser
from constants.http_messages import *
from tara_libot_web_client.models.models import FoodComments, Account
from ..serializers.like_and_unlike_food_serializers import FooodLikeUnlikeSerializer
import pytz
from django.http import Http404 

class LikeAndUnlikeFoodView(APIView):
    def post(self, request, pk):
        errors = {}
        try:
            food_review = FoodComments.objects.get(id=pk)
        except FoodComments.DoesNotExist:
            raise Http404

        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        user = Account.objects.filter(id = payload['id']).first()

        if food_review.likes.filter(id=user.id).exists():
            food_review.likes.remove(user)
            message = "Review unliked successfully."
        else:
            food_review.likes.add(user)
            message = "Review liked successfully."

        food_review.likes.set(food_review.likes.all())
        food_review.save()
        serializer = FooodLikeUnlikeSerializer(food_review)
        data = serializer.data
        status = ok

        return Response({"message": message, "data": data, "status": status, "errors": errors})
    
