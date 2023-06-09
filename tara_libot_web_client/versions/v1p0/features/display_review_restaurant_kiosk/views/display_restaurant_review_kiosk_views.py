from rest_framework.views import APIView
from constants.http_messages import *
import pytz
from rest_framework.response import Response
from ..serializers.display_restaurant_review_kiosk_serializers import DisplayReviewKioskSerializers
from constants.http_messages import *
from django.http import Http404 
from datetime import * 
from tara_libot_web_client.models.models import Business, Comments


class RestaurantReviewKioskListsAPIView(APIView):
    def get(self, request, restaurant_id):
        try:
            restaurant = Business.objects.get(id=restaurant_id)
        except Business.DoesNotExist:
            raise Http404

        reviews = Comments.objects.filter(business=restaurant)
        serializer = DisplayReviewKioskSerializers(reviews, many=True)
        total_reviews = reviews.count()

        data = serializer.data
        total_rating = 0

        for review_data in data:
            review_id = review_data['id']
            review = Comments.objects.get(id=review_id)
            likes_count = review.likes.count()
            review_data['likes_count'] = likes_count

            comment = review_data['created_at']
            comment_dt = datetime.strptime(comment, '%Y-%m-%d')
            review_data['created_at'] = comment_dt.strftime('%Y-%m-%d %I:%M %p')

            total_rating += review.rating

        restaurant_average_rating = round(total_rating / total_reviews, 2) if total_reviews > 0 else None

        status = 'ok'
        message = 'Results'
        errors = {}
        updated_data = {
            "restaurant_name": restaurant.name,
            "total_reviews": total_reviews,
            "restaurant_average_rating": restaurant_average_rating,
            "reviews": data
        }
        data = updated_data

        return Response({"message": message, "data": data, "status": status, "errors": errors})

class DisplayRestaurantKioskDetailReview(APIView):
    def get_restaurant_review(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        phil_tz = pytz.timezone('Asia/Manila')

        comments = self.get_restaurant_review(pk)
        serializer = DisplayReviewKioskSerializers(comments)
        
        data = serializer.data
        data['created_at'] =  comments.created_at.strftime('%Y/%m/%d %H:%M')

        status = 'ok'
        message = 'Results'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})