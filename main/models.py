from django.db import models


# Create your models here.

class StaffModel(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    info = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff', blank=True)
