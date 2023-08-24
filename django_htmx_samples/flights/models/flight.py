from django.db import models

# Create your models here.
class Flight(models.Model):
    plane_name = models.CharField(max_length=60)
    departure = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    additional_information = models.CharField(max_length=120)
