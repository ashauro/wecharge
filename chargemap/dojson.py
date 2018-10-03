from django.core import serializers
from .models import ChargeStation

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

with open ('json.txt', 'w', encoding = 'utf-8') as file:
    file.write(model_station)
