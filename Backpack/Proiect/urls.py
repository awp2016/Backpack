from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^login', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
]