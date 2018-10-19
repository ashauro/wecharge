from django.shortcuts import render
from users.models import Profile, Car


# Create your views here.

def show_profile(request):
    to_page = ''
    for profile in Profile.objects.all():
        to_page += str(profile.user_city)
    return render(request, 'profile.html')