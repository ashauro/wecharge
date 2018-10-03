from django.contrib import admin

# Register your models here.

from .models import ChargeStation, Address, ChargeStationWorkingTime, ChargeStationPlugType, ChargeStationStatus, ChargeStationType

admin.site.register (ChargeStation)
admin.site.register (Address)
admin.site.register (ChargeStationWorkingTime)
admin.site.register (ChargeStationPlugType)
admin.site.register (ChargeStationStatus)
admin.site.register (ChargeStationType)