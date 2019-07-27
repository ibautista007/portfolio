from django.db import models

# Create your models here.
class Designs(models.Model):  
    nSerie = models.CharField(max_length=10)  
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')  
    inventory = models.IntegerField()
    setAlarm = models.IntegerField(default=5)
  
class Shape(models.Model):  
    name = models.CharField(max_length=30)

class Bread(models.Model):  
    name = models.CharField(max_length=30)


