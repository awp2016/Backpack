from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
	Text = models.CharField(max_length=100)
	Date_added = models.DateTimeField(auto_now_add=True)
	Avatar = models.ImageField(null=True, upload_to='images')
	Rating = models.IntegerField()
	#User_id = models.ForeignKey(User,on_delete=models.CASCADE)
	#Destination_id = models.ForeignKey(Destination,on_delete=models.CASCADE)

class Destination (models.Model):
    Destination_name = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    City = models.CharField(max_length=200)





