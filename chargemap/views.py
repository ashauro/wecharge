from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from chargemap.models import ChargeStation

<<<<<<< HEAD
# Create your views here.



def index(request):
	
	data = serializers.serialize("json", ChargeStation.objects.all())
	
	with open ('AllStations.json', 'w', encoding = 'utf-8') as file:
		file.write(data)

	return HttpResponse("JSON is DONE!")

=======

def index(request):
    return render(request, 'index.html')
>>>>>>> c06447c2b78c58699ff5ede3b9b68459c9724e02
