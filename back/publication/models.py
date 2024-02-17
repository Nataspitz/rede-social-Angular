from django.db import models

class Publication(models.Model):
    post = models.TextField(blank=False)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

