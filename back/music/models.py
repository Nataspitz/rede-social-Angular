from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    
