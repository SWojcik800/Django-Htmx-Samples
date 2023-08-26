from django import forms

from flights.models.flight import Flight


class CreateFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['plane_name', 'departure', 'destination', 'departure_time', 'arrival_time', 'additional_information']