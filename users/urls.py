from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_profile, name='Profile'),
    path('update/', views.update_profile, name='Update Profile'),
]