from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name', 'username', 'password')

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField()
    address = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="uploads")
