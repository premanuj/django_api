from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    # username = models.CharField(max_length=50, null=True, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name', 'password')

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField()
    address = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="uploads", null=True)
