from __future__ import unicode_literals

from django.db import models

class Destination (models.Model):
    Destination_name = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    City = models.CharField(max_length=200)

# Create your models here.
