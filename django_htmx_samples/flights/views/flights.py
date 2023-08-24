from django.shortcuts import render
from django.http import HttpResponse

from flights.models.flight import Flight

class Flights:
    def index(request):
        return render(request, "flights/index.html")
    
    def list(request):
        flights = Flight.objects.order_by('-departure_time')
        return render(request, 'flights/list.html', {"items": flights})