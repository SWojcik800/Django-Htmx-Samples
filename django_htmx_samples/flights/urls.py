from django.urls import path

from .views.flights import Flights

urlpatterns = [
    path("", Flights.index),
]