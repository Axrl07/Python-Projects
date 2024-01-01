from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageFacturas, name='homePageFacturas'),
]