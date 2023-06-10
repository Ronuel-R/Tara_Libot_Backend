from rest_framework.views import APIView
from tara_libot_web_client.models.models import FoodComments, Foods
from ..serializers.kiosk_food_review_serializers import KioskFoodReviewSerializers
import datetime
from rest_framework.response import Response
from django.http import Http404
from datetime import *
from constants.http_messages import *
import pytz


class KioskFoodReviewListAPIView(APIView):
    def get(self, request, food_id):
        try:
            food = Foods.objects.get(id=food_id)
        except Foods.DoesNotExist:
            raise Http404

        food_reviews = FoodComments.objects.filter(food=food)
        serializer = KioskFoodReviewSerializers(food_reviews, many=True)

        total_reviews = food_reviews.count()  # Get the total number of reviews
        total_rating = 0
        data = serializer.data
        for review_data in data:
            review_id = review_data['id']
            review = FoodComments.objects.get(id=review_id)
            likes_count = review.likes.count()
            review_data['likes_count'] = likes_count

            food_comment = review_data['created_at']
            food_comment_dt = datetime.strptime(food_comment, '%Y-%m-%d')
            review_data['created_at'] = food_comment_dt.strftime('%Y-%m-%d %I:%M %p')

            total_rating += review.rating

        food_average_rating = round(total_rating / total_reviews, 2) if total_reviews > 0 else None
        status = ok
        message = 'Results'
        errors = {}

        # Update the serializer data to include food_name and total_reviews
        updated_data = {
            "food_name": food.name,
            "food_average_rating":food_average_rating,
            "total_reviews": total_reviews,
            "reviews": data
        }
        data = updated_data
        return Response({"message": message, "data": data, "status": status, "errors": errors})

class DisplayFoodDetailKioskReview(APIView):
    def get_restaurant_review(self, pk):
        try:
            return FoodComments.objects.get(pk=pk)
        except FoodComments.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        phil_tz = pytz.timezone('Asia/Manila')

        comments = self.get_restaurant_review(pk)
        serializer = KioskFoodReviewSerializers(comments)
        
        data = serializer.data
        data['created_at'] =  comments.created_at.strftime('%Y/%m/%d %H:%M')

        status = 'ok'
        message = 'Results'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})