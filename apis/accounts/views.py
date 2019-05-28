from django.shortcuts import render
from rest_framework import viewsets
from apis.accounts.models import UserProfile
from apis.accounts.serializers import UserProfileSerializer

# Create your views here.
class UserAPIView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    