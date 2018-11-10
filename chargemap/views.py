from django.http import HttpResponse
from django.shortcuts import render
from chargemap.models import ChargeStation
import json
from users.forms import ContactIndexForm
from django.core.mail import send_mail, BadHeaderError


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
                 <input type='submit' value='Маршрут'></p>
                 """.format(station.charge_station_name,
                                                        station.charge_station_description,
                                                        station.charge_station_type,
                                                        station.charge_station_maxpower,
                                                        plug_type,
                                                        station.charge_station_status,
                                                        station.charge_station_working_time),
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
    form = ContactIndexForm()
    return render(request, 'index.html', {'form': form, 'mt': 'index'})


def charge_map(request):
    return render(request, 'charge_map.html', {'mt': 'charge_map'})


def contacts(request):
    form = ContactIndexForm()
    return render(request, 'contacts-page.html', {'mt': 'contacts', 'form': form})


def mail_sender(request):
    if request.method == 'POST':
        form = ContactIndexForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            mail_text = """Новое письмо с вашего сайта от пользователя {}!
            Email: {}
            Текст письма: {}
            """.format(name, email, message)
            subject = 'WattsON - форма обратной связи'

            recipients = ['***']
            try:
                send_mail(subject, mail_text, '***', recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'thanks.html')
    else:
        form = ContactIndexForm()
    return render(request, 'index.html', {'form': form})