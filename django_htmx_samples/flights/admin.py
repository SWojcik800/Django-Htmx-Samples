from django.contrib import admin

from flights.models.url_shortcut import UrlShortcut
from flights.models.flight import Flight


# Register your models here.
admin.site.register(Flight)
admin.site.register(UrlShortcut)