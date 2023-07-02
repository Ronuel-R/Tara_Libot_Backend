from rest_framework import serializers
from .......models.models import Marker


class CreateMarkerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    qr_code = serializers.ImageField(read_only=True)

    class Meta:
        model = Marker
        fields = ['id', 'name', 'longitude', 'latitude', 'description', 'qr_code']
