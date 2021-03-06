from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

	url(r'^$', views.ShowDestinations.as_view(), name="destinationss"),
	url(r'^login', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^userProfile/(?P<pk>\d+)/edit/$', views.EditProfile.as_view(), name="editProfile"),
	url(r'^destinations/$', views.ShowDestinations.as_view(), name="destinations"),
	url(r'^destination/(?P<dest_pk>\d+)/$', views.ViewDestination.as_view(), name='viewDest'),
	url(r'^review/(?P<rev_pk>\d+)/$', views.ViewReview.as_view(), name='viewRev'),
	url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile_info'),
	url(r'^add_to_wish_list/(?P<pk_destinatie>\d+)/$',views.create_wishlist_object, name='add_to_wish_list'),
	url(r'^signup/$', views.signup, name="signup"),
    url(r'^wishlist/(?P<pk>\d+)/$', views.ShowWishlist.as_view(), name='wishlist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


