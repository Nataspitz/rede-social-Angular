from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    uid  = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    url_photo = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
    