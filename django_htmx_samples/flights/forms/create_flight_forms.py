from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from flights.models.flight import Flight


class CreateFlightForm(forms.ModelForm):
    departure_time = forms.DateTimeField(
        required=True,
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M:%S']
    )
    arrival_time = forms.DateTimeField(
        required=True,
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M:%S']
    )

    class Meta:
        model = Flight
        fields = ['plane_name', 'departure', 'destination', 'departure_time', 'arrival_time', 'additional_information']