from django.contrib import admin
from .models import Dentist, DentTitle

# Register your models here.
admin.site.register(Dentist)
admin.site.register(DentTitle)