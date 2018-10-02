from django.contrib import admin

# Register your models here.

from .models import ChargeStation, Address, ChargeStationAvailability, ChargeStationPlugType

admin.site.register (ChargeStation)
admin.site.register (Address)
admin.site.register (ChargeStationAvailability)
admin.site.register (ChargeStationPlugType)
