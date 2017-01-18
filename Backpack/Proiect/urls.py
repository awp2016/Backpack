from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^login', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^userProfile/(?P<pk>\d+)/edit/$', views.EditProfile.as_view(), name="editProfile"),
	url(r'^Destinations/$', views.ShowDestinations.as_view(), name="destinations"),
]