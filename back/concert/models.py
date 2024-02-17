from django.db import models

class Concert(models.Model):
    local = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()

    band = models.ForeignKey("band.Band", on_delete=models.CASCADE)
    
