from django.db import models

# Create your models here.

class Dentist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    prof = models.CharField(max_length=100)
    # id:int
    # name: str
    # image: str
    # desc: str
    # prof: str
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    prof = models.CharField(max_length=100)

class Abt_Presonal(models.Model):
    abt_heading1 = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    h1_desc = models.TextField()
    heading21 = models.CharField(max_length=255)
    heading21_desc = models.TextField()
    heading22 = models.CharField(max_length=255)
    heading22_desc = models.TextField()
    heading23 = models.CharField(max_length=255)
    heading23_desc = models.TextField()

class What_we_do(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

class Our_mission(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

class Our_goal(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Slider(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=255)
    desc = models.TextField()

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
