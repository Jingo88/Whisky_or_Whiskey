from django.conf.urls import url
from django.contrib import admin

from .views import(
	posts_list,
	posts_create,
	posts_detail,
	posts_update,
	)

urlpatterns = [
	url(r'^$', posts_list, name='list'),
	url(r'^create$', posts_create, name='create'),
	url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
	url(r'^(?P<id>\d+)/update$', posts_update, name='update'),
]