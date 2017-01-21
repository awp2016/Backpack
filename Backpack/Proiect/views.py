from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms
from django.views.generic.detail import DetailView
from . import models
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


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

def create_wishlist_object(request, destination_id, user_id):
    if request.method == 'POST':
        destination = Destination.objects.get(pk=destination_id)
        user = User.objects.get(pk=user_id)
        Wishlist.object.create(destination, user);
        return redirect('destinations')



class EditProfile(LoginRequiredMixin, UpdateView):
    model = models.UserProfile
    fields = ['First_name', 'Last_name', 'Birthdate', 'Sex', 'Avatar']
    template_name = 'TBackpack/editProfile.html'
    
class ShowDestinations(LoginRequiredMixin, ListView):
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

class ViewReview (DetailView):
    model = models.Review
    template_name = 'TBackpack/review.html'
    pk_url_kwarg = "rev_pk"
    form_class = forms.CommentForm
    def get_context_data(self, **kwargs):
        context = super(ViewReview, self).get_context_data(**kwargs)
        context["comments"] = models.Comment.objects.filter(Review = kwargs['object'].id)
        context["form"] = self.form_class()

        return context

    def post(self, request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = models.Review.objects.get(pk = kwargs['rev_pk'])
            comment = models.Comment.objects.create(Text=form.cleaned_data['Text'],
                                                    Author=request.user,
                                                    Review = review)
            comment.save()
            return redirect('destinations')


    



