from rest_framework import serializers
from apis.accounts.models import User, UserProfile
from django.db import transaction

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        exclude = 'user',
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model= User
        fields = ('url','username', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
    
        UserProfile.objects.create(user=user, **profile_data)
        return user
    
    @transaction.atomic
    def update(self, instance, validated_data):
        pass

