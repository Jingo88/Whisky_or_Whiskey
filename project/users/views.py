from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.views.generic import View

# Create your views here.

class Users_List(View):
	def get(self, req):
		whiskey_list = User.objects.all()
		context = {
			"whiskey_list": whiskey_list,
		}
		return render(req, "user/list.html", context)