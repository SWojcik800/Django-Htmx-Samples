from django.shortcuts import render
from django.http import HttpResponse

class Flights:
    def index(request):
        # Your view logic here
        return render(request, "flights/index.html")