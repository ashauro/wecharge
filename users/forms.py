from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile, Car

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_image', 'user_country','user_city']

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'plate','acc']