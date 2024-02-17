from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    url_photo = models.URLField(blank=True)
    email = models.EmailField(unique=True, max_length=100)
    bio = models.TextField(blank=True)
    