from django.contrib import admin
from .models import Profile, Car, Billing

# Register your models here.

admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Billing)