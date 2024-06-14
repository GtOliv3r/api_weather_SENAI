from rest_framework import serializers
from .models import UserEntity

class UserSerializer(serializers.Serializer):
    
    id = id
    name = serializers.CharField(allow_blank=True, required=False)
    email = serializers.CharField(allow_blank=True, required=False)
    username = serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(allow_blank=True, required=False)

    def create(self, validated_data):
        return UserEntity(**validated_data)