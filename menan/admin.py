from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Testimonials)
admin.site.register(Abt_Presonal)
admin.site.register(Our_goal)
admin.site.register(Our_mission)
admin.site.register(What_we_do)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Contact)

@admin.register(MapSettings)
class MapSettingsAdmin(admin.ModelAdmin):
    list_display = ('map_url',)
    search_fields = ('map_url',)