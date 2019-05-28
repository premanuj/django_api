from rest_framework import serializers
from apis.accounts.models import User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserSerializer()

    class Meta:
        model= UserProfile
        fields = ('dob', 'address', 'avatar', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = profile_data.pop('password')
        user = User(**profile_data)
        user.set_password(password)
        user.save()
    
        UserProfile.objects.create(user=user, **validated_data)
        return user
