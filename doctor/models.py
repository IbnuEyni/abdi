from django.db import models

# Create your models here.

class Dentists(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    prof = models.CharField(max_length=100)
    
    X = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    insta = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)

class DentTitle(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField() 
    opt1 =  models.CharField(max_length=100)
    opt2 =  models.CharField(max_length=100)
    opt3 =  models.CharField(max_length=100)
    opt4 =  models.CharField(max_length=100)
    opt5 =  models.CharField(max_length=100)
class PriTitle(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

class Achievements(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    year_of_exp = models.IntegerField()
    year_of_exp_txt = models.CharField(max_length=255)
    qua_dent = models.IntegerField()
    qua_dent_txt = models.CharField(max_length=255)
    customer = models.IntegerField()
    customer_txt = models.CharField(max_length=255)
    ppy = models.IntegerField()
    ppy_txt = models.CharField(max_length=255) 