from rest_framework import serializers
from tara_libot_web_client.models.models import Foods

class LandingPageKioskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name', 'category', 'price', 'business', 'food_photo']