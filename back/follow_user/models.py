from django.db import models

class Follow_user(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    follower_id = models.CharField(max_length=100)
    followed_id = models.CharField(max_length=100)
