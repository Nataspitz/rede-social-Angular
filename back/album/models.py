from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo_url = models.URLField()
    release_at = models.DateField()
