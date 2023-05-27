from tara_libot_web_client.models.models import Comments
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
import pytz
from constants import http_messages
from ..serializers.add_reviews_serializers import ReviewSerializer
class AddReview(APIView):
    def post(self,request):
        serializer = ReviewSerializer(data= request.data)

        data ={}
        errors ={}
        status = None
        message =None
        

                        
        if serializer.is_valid():
           phil_tz = pytz.timezone
           generate_uid = generate_uid()
           comments = Comments.objects.create(id = generate_uid,
                                              content = request.data['content'],
                                              business = request.data['business'],
                                              rating = mod  
                                              ) 

