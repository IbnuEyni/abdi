from django.contrib import admin
from .models import Dentist, DentTitle, Pricing, PriTitle, Achievements

# Register your models here.
admin.site.register(Dentist)
admin.site.register(DentTitle)
admin.site.register(Pricing)
admin.site.register(PriTitle)
admin.site.register(Achievements)
