from rest_framework import serializers
from......models.models import Comments
class ReviewSerializers(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comments
        fields = ['content','rating','created_by','created_at']
        
        

