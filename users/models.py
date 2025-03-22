from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True) 