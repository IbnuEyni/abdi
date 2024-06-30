from django.db import models

class Smile(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

class Services(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.TextField()
