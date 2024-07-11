from django.db import models

# Create your models here.

class Dentist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    prof = models.CharField(max_length=100)
    X = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    insta = models.CharField(max_length=100)
    google = models.CharField(max_length=100)

class DentTitle(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
