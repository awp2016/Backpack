from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class signupForm(forms.Form):
	username = forms.CharField(label="Username")
	first_name = forms.CharField(label="First_Name")
	last_name = forms.CharField(label="Last_name")
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())