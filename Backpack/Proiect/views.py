from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from . import forms

def login_view(request):
    context = {}
    if request.method == 'GET':
        form = forms.LoginForm()
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('index')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'TBackpack/login.html', context)

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')