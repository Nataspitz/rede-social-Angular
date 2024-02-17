from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    publication = models.ForeignKey("publication.Publication", on_delete=models.CASCADE)
