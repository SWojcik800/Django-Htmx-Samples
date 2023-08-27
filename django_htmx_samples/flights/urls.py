from django.urls import path

from .views.flights import Flights

urlpatterns = [
    path("", Flights.index, name='index'),
    path("list", Flights.list, name='flights-list'),
    # path("list/<int:page_index>", Flights.list, name='flights-list'),
    path("create", Flights.create, name='flights-create'),
    path("create-btn", Flights.create_btn, name='flights-create-btn'),
    path("edit/<int:id>", Flights.edit, name='flights-edit')
]