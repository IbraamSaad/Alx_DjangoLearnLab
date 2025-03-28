from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

"Token.objects.create", "get_user_model().objects.create_user"

User = get_user_model()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    bio = serializers.CharField(allow_blank=True, required=False)
    profile_picture = serializers.ImageField(allow_null=True, required=False)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture'),
        )

class TokenSerializer(serializers.Serializer):
    key = serializers.CharField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)