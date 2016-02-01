from django.conf.urls import url
from django.contrib import admin

###########################################################################
##########	URL Patters Class Based Views		###############
###########################################################################
from .views import(
	Users_List,
	# Users_Create,
	# Users_Detail,
	# Users_Update,
	# Users_Delete,
	)

urlpatterns = [
	url(r'^$', Users_List.as_view(), name='list'),
	# url(r'^create$', Posts_Create.as_view(), name='create'),
	# url(r'^(?P<id>\d+)/$', Posts_Detail.as_view(), name='detail'),
	# url(r'^(?P<id>\d+)/update$', Posts_Update.as_view(), name='update'),
	# url(r'^(?P<id>\d+)/delete$', Posts_Delete.as_view(), name='delete'),	
]