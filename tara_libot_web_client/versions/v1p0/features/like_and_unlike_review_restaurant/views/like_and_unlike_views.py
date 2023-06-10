from rest_framework.response import Response
from rest_framework.views import APIView
from constants.auth_user import AuthUser
from constants.http_messages import *
from tara_libot_web_client.models.models import Comments, FoodComments, Account
from ..serializers.like_serializers import LikeSerializer
import pytz
from django.http import Http404 

class LikeAndUnlikeView(APIView):
    def post(self, request, pk):
        errors = {}
        try:
            review = Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            raise Http404

        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        user = Account.objects.filter(id = payload['id']).first()

        if review.likes.filter(id=user.id).exists():
            review.likes.remove(user)
            message = "Review unliked successfully."
        else:
            review.likes.add(user)
            message = "Review liked successfully."

        review.likes.set(review.likes.all())
        review.save()
        serializer = LikeSerializer(review)
        data = serializer.data
        status = ok

        return Response({"message": message, "data": data, "status": status, "errors": errors})
    
