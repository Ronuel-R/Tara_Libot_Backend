from django.contrib import admin
from tara_libot_web_client.models.models import *
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
admin.site.register(Foods)


admin.site.register(Comments)
admin.site.register(Account)
admin.site.register(Business)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')