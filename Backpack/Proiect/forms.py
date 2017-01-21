from django import forms
from django.forms import ModelForm
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ReviewForm(ModelForm):

    Rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    class Meta:
        model = models.Review
        fields = ['Text','Photo','Rating']
        exclude = ['Date_added']