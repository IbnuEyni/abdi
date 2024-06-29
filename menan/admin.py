from django.contrib import admin

from .models import Dentist, Testimonials

# Register your models here.
admin.site.register(Dentist)
admin.site.register(Testimonials)