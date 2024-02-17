from django.db import models

class Follow_band(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    band = models.ForeignKey("band.Band", on_delete=models.CASCADE)
