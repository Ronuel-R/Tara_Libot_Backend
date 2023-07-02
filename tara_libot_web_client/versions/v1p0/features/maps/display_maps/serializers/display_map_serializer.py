from rest_framework import serializers
from .......models.models import Marker


class DisplayMarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['id','name', 'longitude', 'latitude', 'description', 'qr_code']