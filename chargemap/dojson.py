from chargemap.models import ChargeStation
from django.http import HttpResponse
import json


def dojson(request):
    all_stations_json = {"type": "FeatureCollection", "features": []}
    baloon_preset = ''
    for station in ChargeStation.objects.all():
        plug_type = ''
        if str(station.status) == 'Нет данных':
            baloon_preset = 'islands#greyDotIcon'
        elif str(station.status) == 'Оффлайн':
            baloon_preset = 'islands#blackDotIcon'
        elif str(station.status) == 'Онлайн':
            baloon_preset = 'islands#darkGreenDotIcon'

        for plug in station.plug.all():
            plug_type += " %s " % str(plug)
        json_station = {"type": "Feature", "id": station.pk, "geometry":
            {"type": "Point", "coordinates": [station.latitude,
                                              station.longtitude]},
             "properties": {
                "balloonContent": """<h4><b>{1}</b></h4>
                <p><i>{2}</i></p>
                <p>{3}</p>
                 <b>Тип зарядки:</b> {4}<br>
                 <b>Мощность:</b> {5}<br>
                 <b>Тип разъема:</b> {6}<br>
                 <b>Статус:</b> {7}<br>
                 <b>Время работы:</b> {8}<br><br>
                 <p><input type='submit' value='Забронировать' onclick="javascript:window.location='detail/{0}'">
                 <input type='submit' value='Маршрут' onclick = 'getroute({9},{10})'></p>
                 """.format(station.id, 
                                                        station.name,
                                                        station.address,
                                                        station.description,
                                                        station.station_type,
                                                        station.maxpower,
                                                        plug_type,
                                                        station.status,
                                                        station.working_time,
                                                        station.latitude,
                                                        station.longtitude),
                "hintContent": station.name
            },
            "options": {
                "preset": baloon_preset
            }
                        }
        all_stations_json["features"].append(json_station)
    with open('static/js/data.json', 'w', encoding='utf-8', ) as json_file:
        json.dump(all_stations_json, json_file, ensure_ascii=False, indent=4)

    return HttpResponse('Json готов!')