from rest_framework import serializers
from tara_libot_web_client.models.models import FoodComments
class FooodLikeUnlikeSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = FoodComments
        fields = ['id', 'content', 'food', 'rating', 'created_at', 'created_by', 'likes']

    def get_created_by(self, obj):
        user = obj.created_b
        return {
            'id': user.id,
            'username': user.user.username,
            'email': user.user.email
        }