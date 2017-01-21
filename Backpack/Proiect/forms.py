from django import forms
from django.forms import ModelForm
from Proiect.models import Comment

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class CommentForm(ModelForm):
	class Meta:
	    model = Comment
	    fields = ['Text', 'Author']
	    exlude = ['Date_added']



