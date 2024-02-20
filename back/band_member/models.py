from django.db import models

class Band_member(models.Model):
    main_function = models.CharField(max_length=50)
    member_since = models.DateField()

    member_id = models.CharField(max_length=100)
    band_id = models.CharField(max_length=100)
