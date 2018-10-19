from django.shortcuts import render
from users.models import Profile, Car


# Create your views here.

def show_profile(request):
    return render(request, 'profile.html')