from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.posts.models import Post, Comment
from apis.posts.serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
# Create your views here.

class PostView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, pk=None):
        if pk:
            post = get_object_or_404(Post.objects.all(), pk=pk)
            serializer = PostSerializer(post)
            return Response({"post":serializer.data})

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # if serializer.is_valid(raise_exception=True):
        return Response({"posts":serializer.data})

    def post(self, request):
        post = request.data.get('post')
        post["slug"] = slugify(post['title'])
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"post":serializer.data})

class CommentView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, post_id=None):
        if post_id:
            comments = Comment.objects.filter(post=post_id)
            serializer = CommentSerializer(comments, many=True)
            # if serializer.is_valid(raise_exception=True):
            return Response({"comments":serializer.data})

    def post(self, request, post_id=None):
        comment = request.data.get('comment')
        post = comment.get('post')
        if post == post_id:
            serializer = CommentSerializer(data=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"comment":serializer.data})
        return Response({"error":"No post matched."})


