from django.contrib import admin

from .models import LocationInfo, VisitedLocationInfo, LocationDetails
# Register your models here.

admin.site.register(LocationInfo)
admin.site.register(VisitedLocationInfo)
admin.site.register(LocationDetails)
