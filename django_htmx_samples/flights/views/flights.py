from django.shortcuts import get_object_or_404, render
from flights.forms.create_flight_forms import CreateFlightForm
from flights.forms.edit_flight_form import EditFlightForm

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
        form = CreateFlightForm(request.POST or None)

        if request.method == 'GET':
            return render(request, 'flights/create.html', {"form": form})

        if form.is_valid():
            createdFlight = form.save()
            response = render(request, 'flights/list-item.html', {"item": createdFlight})
            response['HX-Trigger'] = 'flight-created'
            response['HX-Reswap'] = 'delete'
            return response
        
        return render(request, 'flights/create.html', {"form": form})
        
    def create_btn(request):
        return render(request, 'flights/create-btn.html')
    
    def edit(request, id):
        editedFlight = get_object_or_404(Flight, pk=id)
        if request.method == 'GET':
            form = EditFlightForm(instance=editedFlight)
            return render(request, 'flights/edit.html', {"form": form, "id": editedFlight.pk})

        form = EditFlightForm(request.POST, instance=editedFlight)
        if form.is_valid():
            updatedFlight = form.save()
            response = render(request, 'flights/list-item.html', {"item": updatedFlight, "id": editedFlight.pk})
            response['HX-Trigger'] = 'flight-created'
            return response
        
        return render(request, 'flights/edit.html', {"form": form, "id": editedFlight.pk})

    def get(request, id):
        flight = get_object_or_404(Flight, pk=id)
        return render(request, 'flights/list-item.html', {"item": flight, "id": flight.pk})
        