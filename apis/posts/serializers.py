from apis.posts.models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = "__all__"
        # exclude = ('created_at', 'updated_at', 'slug')

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Comment
        exclude = ('created_at', 'updated_at')
