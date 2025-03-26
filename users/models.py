from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# 重要：在users/apps.py中添加
# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'users' 