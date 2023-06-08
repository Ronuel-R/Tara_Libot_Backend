from ......models.models import Comments, Business, Account
from rest_framework.views import APIView
import pytz
from rest_framework.response import Response

from ..serializers.display_review_serializers import DisplayReviewSerializers
from constants.http_messages import *
from django.http import Http404 
from constants.auth_user import AuthUser
from datetime import *






class DisplayRestaurantDetailReview(APIView):
    def get_restaurant_review(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        phil_tz = pytz.timezone('Asia/Manila')

        comments = self.get_restaurant_review(pk)
        serializer = DisplayReviewSerializers(comments)
        
        data = serializer.data
        data['created_at'] =  comments.created_at.strftime('%Y/%m/%d %H:%M')

        status = 'ok'
        message = 'Results'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})

class DisplayRestaurantReview(APIView):

    def get(self, request):
        serializer = DisplayReviewSerializers
        phil_tz = pytz.timezone('Asia/Manila')
        comments = Comments.objects.all()

        serialized_comments = serializer(comments, many=True).data

        for comment in serialized_comments:
            created_at = comment['created_at']
            created_dt = datetime.strptime(created_at, '%Y-%m-%d')
            comment['created_at'] = created_dt.strftime('%Y-%m-%d %I:%M %p')

        data = serialized_comments
        message = 'Success'
        status = 'ok'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})
        
class RestaurantReviewListAPIView(APIView):
    def get(self, request, restaurant_id):
        try:
            restaurant = Business.objects.get(id=restaurant_id)
        except Business.DoesNotExist:
            raise Http404

        reviews = Comments.objects.filter(business=restaurant)
        serializer = DisplayReviewSerializers(reviews, many=True)
        total_reviews = reviews.count()

        data = serializer.data
        for review_data in data:
            review_id = review_data['id']
            review = Comments.objects.get(id=review_id)
            likes_count = review.likes.count()
            review_data['likes_count'] = likes_count

            comment = review_data['created_at']
            comment_dt = datetime.strptime(comment, '%Y-%m-%d')
            review_data['created_at'] = comment_dt.strftime('%Y-%m-%d %I:%M %p')

        status = 'ok'
        message = 'Results'
        errors = {}
        updated_data = {
            "restaurant_name": restaurant.name,
            "total_reviews": total_reviews,
            "reviews": data
        }
        data = updated_data

        return Response({"message": message, "data": data, "status": status, "errors": errors})
