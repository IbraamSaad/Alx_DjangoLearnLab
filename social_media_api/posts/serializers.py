from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer  

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'author')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'author')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
