from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from chargemap.models import ChargeStation


# Create your views here.

#def dojson(request):
#	data = serializers.serialize("json", ChargeStation.objects.all())
#	with open ('AllStations.json', 'w', encoding = 'utf-8') as file:
#		file.write(data)
#
#	return HttpResponse("JSON is DONE!")


def dojson(request):
	json = ''
	i = 1
	for station in ChargeStation.objects.all():
		station = ChargeStation.objects.get(id=i)
		json = { "type": "FeatureCollection", "features": [{"type": "Feature", "id": i, "geometry": {"type": "Point", "coordinates": [station.charge_station_latitude, station.harge_station_longtitude]}}]}
		i += 1
		with open ('static/js/data.json', 'w', encoding = 'utf-8') as file_to_write:
			json = str(json).replace('\'','"')
			file_to_write.write(str(json))
			print (json)
		return HttpResponse("JSON готов!")



def index(request):
    return render(request, 'index.html')
