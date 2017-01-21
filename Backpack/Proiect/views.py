from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import forms
from django.views.generic.detail import DetailView
from . import models
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from models import Review,Destination
from django.http import HttpResponse

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
    

class ShowDestinations(ListView):

    def get_success_url(self, **kwargs):
        #import pdb; pdb.set_trace()
        return reverse_lazy('profile_info', kwargs = {'pk': self.object.User.id})
	

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
    
    form_class = forms.ReviewForm
    pk_url_kwarg = "dest_pk"
    
    def get_context_data(self, **kwargs):
        context = super(ViewDestination, self).get_context_data(**kwargs)
        context["reviews"] = models.Review.objects.filter(Destination_id = kwargs['object'].id)
        context["form"] = self.form_class()

        s = 0
        for r in context['reviews']:
            s = s + r.Rating

        if len(context['reviews']) != 0:
            context["grade"] = s/len(context['reviews'])
        else:
            context["grade"] = 0
        return context
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        import pdb;pdb.set_trace()
        if form.is_valid():
            destination = Destination.objects.get(pk=kwargs["dest_pk"])
            revi = Review.objects.create(Text=form.cleaned_data['Text'],
                            Photo=form.cleaned_data['Photo'],
                            Rating=form.cleaned_data['Rating'],
                            User_id=request.user,
                            Destination_id=destination,
                            )
        return redirect("destinations")

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

        
def signup(request):
    context = {}
    if request.method == "GET":
        context['form'] = forms.signupForm()
        return render(request, 'TBackpack/signup.html', context=context)
    form = forms.signupForm(request.POST)
    #import pdb 
    #pdb.set_trace()
    if request.method == "POST":
        if form.is_valid(): 
            username = form.cleaned_data['username']
            First_name = form.cleaned_data['first_name']
            Last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            if User.objects.filter(username=username).exists():
                return HttpResponse('<p>Username exista!!!</p>')
            new_user = User.objects.create_user(username=username, first_name=First_name, last_name=Last_name, password=password1)
            login(request, new_user)
            return redirect('destinations')
        return HttpResponse(form.errors)
    


class ShowWishlist(LoginRequiredMixin, ListView):
    model = models.Wishlist
    template_name = 'TBackpack/wishlist.html'
    pk_url_kwarg = "pk"


    def get_context_data(self, **kwargs):
        context = {}
        context["wishlist"] = models.Wishlist.objects.filter(User_id = self.request.user.id)
        return context


