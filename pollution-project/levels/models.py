from django.db import models

# Create your models here.
class pollution_index(models.Model):
    city =  models.CharField(max_length = 20)
    date =  models.DateField()
    pm25 =  models.IntegerField()
    pm10 =  models.IntegerField()
    o3   =  models.IntegerField()
    no2  =  models.IntegerField()
    so2  =  models.IntegerField()
    co   =  models.IntegerField()
