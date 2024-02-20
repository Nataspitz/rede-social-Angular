from django.db import models

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_like = models.BooleanField(default=False)
    
    user_id = models.CharField(max_length=100)
    publication_id = models.CharField(max_length=100)
