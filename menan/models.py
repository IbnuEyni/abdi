from django.db import models

# Create your models here.


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

class MapSettings(models.Model):
    map_url = models.URLField(help_text="Enter the Google Maps embed URL here.")

    def __str__(self):
        return "Map Settings"

    class Meta:
        verbose_name = "Map Setting"
        verbose_name_plural = "Map Settings"


class Appointments(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    appointment_date = models.DateTimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.appointment_date}"