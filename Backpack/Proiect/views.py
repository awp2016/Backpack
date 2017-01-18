from django.shortcuts import render
from django.views.generic.detail import DetailView
from . import models



class ProfileView(DetailView):

    model = models.UserProfile
    template_name = 'TBackpack/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

