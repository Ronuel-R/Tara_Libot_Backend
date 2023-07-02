from rest_framework import serializers
from .......models.models import Marker


class UpdateMarkerSerializer(serializers.ModelSerializer):
    qr_code = serializers.ImageField(read_only=True)
    class Meta:
        model = Marker
        fields = ['id','name', 'longitude', 'latitude', 'description', 'qr_code']