from django.urls import path

from .views.flights import Flights
from .views.url_shortcuts import UrlShortcutsIndex
from .views.url_shortcuts import UrlShortcutsRows

urlpatterns = [
    path("", Flights.index, name='index'),
    path("list", Flights.list, name='flights-list'),
    # path("list/<int:page_index>", Flights.list, name='flights-list'),
    path("create", Flights.create, name='flights-create'),
    path("create-btn", Flights.create_btn, name='flights-create-btn'),
    path("edit/<int:id>", Flights.edit, name='flights-edit'),
    path("get/<int:id>", Flights.get, name='flights-get'),
    path("url-shortcuts/", UrlShortcutsIndex.as_view(), name='url_shortcuts_index'),
    path("url-shortcuts/rows", UrlShortcutsRows.as_view(), name='url_shortcuts_rows')
]