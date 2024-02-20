from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user_id = models.CharField(max_length=100)
    publication_id = models.CharField(max_length=100)
