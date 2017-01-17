from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
	Text = models.CharField(max_length=200)
    Date_added = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User)
    
    
class Wishlist(models.Model)
	Destination_id = models.ForeignKey(Destination)
	User_id = models.ForeignKey(User)
