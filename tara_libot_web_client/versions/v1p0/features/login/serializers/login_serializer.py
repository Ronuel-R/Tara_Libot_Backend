from rest_framework import serializers
from django.contrib.auth.models import User


class LoginAdminSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['email','password']