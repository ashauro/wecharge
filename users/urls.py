from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_profile, name='Profile'),
]