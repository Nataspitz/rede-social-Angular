from django.db import models

class Follow_band(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    user_id = models.CharField(max_length=100)
    band_id = models.CharField(max_length=100)
