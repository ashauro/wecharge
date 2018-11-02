from django.views import generic
from django.shortcuts import render
from chargemap.dojson import dojson
from .models import ChargeStation 


class DetailStationView(generic.DeleteView):
    model = ChargeStation
    template_name = 'chargemap/detail.html'

class ManagementView(generic.DeleteView):
    model = ChargeStation
    template_name = 'chargemap/management.html'

def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')