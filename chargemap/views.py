from django.http import HttpResponse
from django.shortcuts import render
from chargemap.models import ChargeStation
import json


def dojson(request):
    all_stations_json = {"type": "FeatureCollection", "features": []}
    for station in ChargeStation.objects.all():
        json_station = {"type": "Feature", "id": station.pk, "geometry":
            {"type": "Point", "coordinates": [station.charge_station_latitude,
                                              station.charge_station_longtitude]},
             "properties": {
                "balloonContent": """<h4><b>{0}</b></h4>
                <p>{1}</p>
                 <b>Тип зарядки:</b> {2}<br>
                 <b>Мощность:</b> {3}<br>
                 <b>Тип разъема:</b> {4}<br>
                 <b>Статус:</b> {5}<br>
                 <b>Время работы:</b> {6}<br>""".format(station.charge_station_name,
                                                        station.charge_station_description,
                                                        station.charge_station_type,
                                                        station.charge_station_maxpower,
                                                        station.charge_station_plug,
                                                        station.charge_station_status,
                                                        station.charge_station_working_time),
                "hintContent": station.charge_station_name
            },
            "options": {
                "preset": "islands#greenDotIcon"
            }
                        }
        all_stations_json["features"].append(json_station)
    with open('static/js/data.json', 'w', encoding='utf-8', ) as json_file:
        json.dump(all_stations_json, json_file, ensure_ascii=False, indent=4)
    return HttpResponse("JSON готов!")


def index(request):
    return render(request, 'index.html')
