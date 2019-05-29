from django.shortcuts import render
from rest_framework import viewsets
from apis.accounts.models import UserProfile, User
from apis.accounts.serializers import UserProfileSerializer, UserSerializer

# Create your views here.
class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    