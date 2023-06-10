from rest_framework import serializers
from tara_libot_web_client.models.models import Comments
class LikeSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['id', 'content', 'business', 'rating', 'created_at', 'created_by', 'likes']

    def get_created_by(self, obj):
        user = obj.created_by
        return {
            'id': user.id,
            'username': user.user.username,
            'email': user.user.email
        }