from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.views.generic import View
from django import forms
from .forms import UserForm

# Create your views here.

class Users_Profile(View):
	profile_template = 'users/profile.html'

	def get(self, req):
		users = User.objects.all()
		context = {
			"users": users,
		}
		return render(req, self.profile_template, context)

class Users_Register(View):
	register_template = 'users/register.html'
	profile_view = "users:profile"
	form_class = UserForm
	initial = {'key': 'value'}	

	def get(self, req, *args, **kwargs):
		register_form = self.form_class(initial = self.initial)
		context = {
			"register": register_form
		}
		return render(req, self.register_template, context)

	def post(self, req, *args, **kwargs):
		register_form = self.form_class(req.POST or None)
		if register_form.is_valid():
			instance = register_form.save(commit=False)
			instance.save()
			return redirect(self.profile_view)
		context = {
			"register": register_form
		}
		return render(req, self.profile_view, context)

# class Users_Login(View):
# 	form_class = UserForm
# 	login_template = "users/login.html"

# 	def get(self, req, *args, **kwargs):
# 		user = get_object_or_404(User, id=kwargs['id'])
# 		user_form = self.form_class(req.POST or None, instance = user)
# 		context = {
# 			"user": user_form
# 		}
# 		return render(req, self.login_template, context)








# Should class register and class login be the same thing?










