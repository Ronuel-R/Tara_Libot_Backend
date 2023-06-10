from rest_framework import serializers
from tara_libot_web_client.models.models import Comments, Account


class DisplayReviewSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        account = obj.created_by
        return AccountSerializer(account).data
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    class Meta: 
        model= Comments
        fields = ['id','content', 'rating', 'user', 'created_at', 'likes','likes_count']

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Account
        fields = ['username', 'profile_picture', 'age', 'date_of_birth', 'gender', 'phone_num', 'created', 'modified']

