from rest_framework import serializers
from tara_libot_web_client.models.models import Business

class BusinessKioskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name', 'address', 'city', 'business_photo', 'rating', 'closing_time','opening_time']