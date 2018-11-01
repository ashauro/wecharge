from django.http import HttpResponse
from django.shortcuts import render
from chargemap.models import ChargeStation
import json


def dojson(request):
    all_stations_json = {"type": "FeatureCollection", "features": []}
    baloon_preset = ''
    for station in ChargeStation.objects.all():
        plug_type = ''
        if str(station.charge_station_status) == 'Нет данных':
            baloon_preset = 'islands#greyDotIcon'
        elif str(station.charge_station_status) == 'Оффлайн':
            baloon_preset = 'islands#blackDotIcon'
        elif str(station.charge_station_status) == 'Онлайн':
            baloon_preset = 'islands#darkGreenDotIcon'

        for plug in station.charge_station_plug.all():
            plug_type += "/%s/" % str(plug)
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
                 <b>Время работы:</b> {6}<br><br>
                 <p><input type='submit' value='Забронировать'>
                 <input type='submit' value='Маршрут' onclick = 'getroute({7},{8})'></p>
                 """.format(station.charge_station_name,
                                                        station.charge_station_description,
                                                        station.charge_station_type,
                                                        station.charge_station_maxpower,
                                                        plug_type,
                                                        station.charge_station_status,
                                                        station.charge_station_working_time,
                                                        station.charge_station_latitude,
                                                        station.charge_station_longtitude),
                "hintContent": station.charge_station_name
            },
            "options": {
                "preset": baloon_preset
            }
                        }
        all_stations_json["features"].append(json_station)
    with open('static/js/data.json', 'w', encoding='utf-8', ) as json_file:
        json.dump(all_stations_json, json_file, ensure_ascii=False, indent=4)

    return HttpResponse(station.charge_station_status)



def index(request):
    return render(request, 'index.html')
