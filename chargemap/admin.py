from django.contrib import admin

# Register your models here.

from .models import ChargeStation, Country, City, ChargeStationWorkingTime, ChargeStationPlugType, ChargeStationStatus, ChargeStationType, StationOperator

admin.site.register (ChargeStation)
admin.site.register (StationOperator)
admin.site.register (Country)
admin.site.register (City)
admin.site.register (ChargeStationWorkingTime)
admin.site.register (ChargeStationPlugType)
admin.site.register (ChargeStationStatus)
admin.site.register (ChargeStationType)