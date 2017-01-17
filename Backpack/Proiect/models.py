from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Status(models.Model):
	Text = models.CharField(max_length=100)
	Date_added = models.DateTimeField(auto_now_add=True)
	Avatar = models.ImageField(null=True, upload_to='images')
	Rating = models.IntegerField()
	User_id = models.ForeignKey(User,on_delete=models.CASCADE)
	Destination_id = models.ForeignKey(Destination,on_delete=models.CASCADE)



