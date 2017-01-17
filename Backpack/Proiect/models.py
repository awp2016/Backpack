from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Birthdate = models.DateField(null=True)
    Sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=FEMALE)
    Avatar = models.ImageField(null=True, upload_to='Avatars')
    #User = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete = models.CASCADE)
