from rest_framework import serializers
from tara_libot_web_client.models.models import FoodComments, Account


class DisplayFoodReviewSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    

    def get_user(self, obj):
        account = obj.created_by
        return AccountSerializer(account).data
    
    class Meta: 
        model= FoodComments
        fields = ['user','content', 'food', 'rating', 'created_by', 'created_at', 'likes' ]

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Account
        fields = ['username', 'profile_picture', 'age', 'date_of_birth', 'gender', 'phone_num', 'created', 'modified']

