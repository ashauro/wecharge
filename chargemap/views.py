from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from chargemap.models import ChargeStation


# Create your views here.

def dojson(request):
    json_dict = {
        "type": "FeatureCollection",
        "features": [
            {"type": "Feature", "id": 0, "geometry": {"type": "Point", "coordinates": [55.831903, 37.411961]}},
            {"type": "Feature", "id": 1, "geometry": {"type": "Point", "coordinates": [55.763338, 37.565466]}},
            {"type": "Feature", "id": 2, "geometry": {"type": "Point", "coordinates": [55.763338, 37.616378]}}
        ]
    }
    model_station = ChargeStation.objects.all()
    for station in model_station:
        print(station.charge_station_latitude)
    return HttpResponse("JSON is DONE!")


def index(request):
    return render(request, 'index.html')
