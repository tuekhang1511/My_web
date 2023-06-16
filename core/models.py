
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from puddle import settings

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

# myapp/models.py
from django.contrib.auth.models import AbstractUser

def user_avatar_upload_path(instance, filename):
    # Generate the upload path for the avatar
    return f'avatars/user_{instance.id}/{filename}'

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.jpg')
    email_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username
