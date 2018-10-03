from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from chargemap.models import ChargeStation


# Create your views here.

def json(request):
	
	data = serializers.serialize("json", ChargeStation.objects.all())
	
	with open ('AllStations.json', 'w', encoding = 'utf-8') as file:
		file.write(data)

	return HttpResponse("JSON is DONE!")


def index(request):
    return render(request, 'index.html')
