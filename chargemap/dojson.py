from django.core import serializers
import models

data = serializers.serialize("xml", ChargeStation.objects.all())

with open ('json.txt', 'w', encoding = 'utf-8') as file:
    file.write(data)


