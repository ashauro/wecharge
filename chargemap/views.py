from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from chargemap.models import ChargeStation
import json


def dojson(request):
    all_stations_list = {"type": "FeatureCollection", "features": []}
    for station in ChargeStation.objects.all():
        json_station = {"type": "Feature", "id": station.pk,
                "geometry": {"type": "Point",
                             "coordinates": [station.charge_station_latitude,
                                             station.charge_station_longtitude]}}
        all_stations_list["features"].append(json_station)
    with open('static/js/data.json', 'w', encoding='utf-8') as file_to_write:
        json.dump(all_stations_list, file_to_write)
    return HttpResponse("JSON готов!")


def index(request):
    return render(request, 'index.html')
