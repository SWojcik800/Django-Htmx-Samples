from django.shortcuts import render
from django.http import HttpResponse
from flights.forms.create_flight_forms import CreateFlightForm

from flights.models.flight import Flight

class Flights:
    def index(request):
        return render(request, "flights/index.html")
    
    def list(request):
        page_index = int(request.GET.get('page_index', '1'))
        page_size = 10
        keyword = request.GET.get('keyword')
        offset = (page_index-1) * page_size
        limit = page_size

        query = Flight.objects

        if keyword is not None:
            query = query.filter(plane_name__startswith=keyword)

        flights = query.order_by('-departure_time')[offset:offset + limit]
        total_count = query.count()

        pages = (total_count + page_size - 1) // page_size
        return render(request, 'flights/list.html',
                       {
                        "items": flights, 
                        "pages": range(1,pages+1),
                        "current_page": page_index,
                        "keyword": keyword
                        })
    
    def create(request):

        if request.method == 'GET':
            form = CreateFlightForm()
            return render(request, 'flights/create.html')
        form = CreateFlightForm(request.POST)

        if form.is_valid():
            createdFlight = form.save()
            response = render(request, 'flights/list-item.html', {"item": createdFlight})
            response['HX-Trigger'] = 'flight-created'
            response['HX-Reswap'] = 'delete'
            return response
        
        return render(request, 'flights/create.html', {"form": form})
        
    def create_btn(request):
        return render(request, 'flights/create-btn.html')

        