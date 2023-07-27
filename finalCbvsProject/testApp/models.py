from django.db import models

# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=70)
    taste= models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    price = models.FloatField()