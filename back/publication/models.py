from django.db import models

class Publication(models.Model):
    user_id = models.CharField(max_length=100)  
    post = models.TextField(blank=False)
    video_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

