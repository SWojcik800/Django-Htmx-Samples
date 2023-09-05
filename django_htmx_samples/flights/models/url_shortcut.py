from django.db import models

class UrlShortcut(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField(max_length=255)
    valid_to = models.DateTimeField()