from rest_framework import serializers
from tara_libot_web_client.models.models import FoodComments

class FoodReviewSerializers(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FoodComments
        fields = ['content','rating','created_by','created_at']


