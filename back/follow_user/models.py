from django.db import models

class Follow_user(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    following = models.ForeignKey("user.User", on_delete=models.CASCADE)
    followed = models.ForeignKey("user.User", on_delete=models.CASCADE)
