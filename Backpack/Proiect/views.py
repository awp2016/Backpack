from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms
from django.views.generic.detail import DetailView
from . import models
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfileView(DetailView):

    model = models.UserProfile
    template_name = 'TBackpack/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context


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
                return redirect('destinations')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'TBackpack/login.html', context)

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


class EditProfile(LoginRequiredMixin, UpdateView):
    model = models.UserProfile
    fields = ['First_name', 'Last_name', 'Birthdate', 'Sex', 'Avatar']
    template_name = 'TBackpack/editProfile.html'
    

class ShowDestinations(ListView):

    def get_success_url(self, **kwargs):
        #import pdb; pdb.set_trace()
        return reverse_lazy('profile_info', kwargs = {'pk': self.object.User.id})
	

class ShowDestinations(LoginRequiredMixin, ListView):
>>>>>>> 04bae193c09e1f64359dd3eb46dd1bd6cfa2c0ca
    model = models.Destination
    template_name = 'TBackpack/destinations.html'

    def get_context_data(self, **kwargs):
        context = super(ShowDestinations, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.order_by('Destination_name')
        
class ViewDestination (DetailView):
    model = models.Destination
    template_name = 'TBackpack/destination.html'
    pk_url_kwarg = "dest_pk"
    
    def get_context_data(self, **kwargs):
        context = super(ViewDestination, self).get_context_data(**kwargs)
        context["reviews"] = models.Review.objects.filter(Destination_id = kwargs['object'].id)
        return context


class ShowWishlist(LoginRequiredMixin, ListView):
    model = models.Wishlist
    template_name = 'TBackpack/wishlist.html'
    pk_url_kwarg = "pk"


    def get_context_data(self, **kwargs):
        context = {}
        context["wishlist"] = models.Wishlist.objects.filter(User_id = self.request.user.id)
        return context

