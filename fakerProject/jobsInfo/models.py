from django.db import models
# Create your models here.
class hydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    PhoneNumber=models.BigIntegerField()

class BengaluruJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    PhoneNumber=models.BigIntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    PhoneNumber=models.BigIntegerField()