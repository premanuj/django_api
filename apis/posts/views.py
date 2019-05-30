from django.shortcuts import render
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.posts.models import Post, Comment
from apis.posts.serializers import PostSerializer, CommentSerializer
# Create your views here.

class PostView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        return Response(posts)

    def post(self, request):
        serializer = PostSerializer()
        data = serializer.data
        # data['slug'] = slugify(data['title'])
        # post = Post.objects.create(**data)
        post = Post(**data)
        post.slug = slugify(data['title'])
        post.author = request.user
        post.save()
        return Response(post)
