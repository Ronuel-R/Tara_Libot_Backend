from django.contrib import admin
from tara_libot_web_client.models.models import *
from mapbox_location_field.admin import MapAdmin
from django.conf import settings

class BusinessMapAdmin(MapAdmin):
    mapbox_key = settings.MAPBOX_KEY
    mapbox_view = 'mapbox://styles/mapbox/streets-v11'
# Register your models here.
admin.site.register(Foods)
admin.site.register(Comments)
admin.site.register(Account)
admin.site.register(Business, BusinessMapAdmin)
admin.site.register(FoodComments)
admin.site.register(Marker)