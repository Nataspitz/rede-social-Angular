from django.db import models

class Band_member(models.Model):
    main_function = models.CharField(max_length=50)
    member_since = models.DateField()

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    band = models.ForeignKey("band.Band", on_delete=models.CASCADE)
