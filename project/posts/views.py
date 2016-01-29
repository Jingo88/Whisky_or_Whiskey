from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Post
from posts.forms import PostForm

# Create your views here.

def posts_list(req):
	whiskey_list = Post.objects.all()
	context = {
		"whiskey_list" : whiskey_list,
	}
	return render(req, "posts/list.html", context)

def posts_create(req):
	create_form = PostForm(req.POST or None)

	if create_form.is_valid():
		instance = create_form.save(commit=False)
		instance.save()
		# return HttpReponseRedirect(instance.get_absolute_url())
		return redirect(instance)
	context = {
		"create":create_form,
	}
	return render(req, "posts/create.html", context)

def posts_detail(req, id=None):
	whiskey = get_object_or_404(Post, id=id)
	print(whiskey.id)
	context = {
		"whiskey": whiskey
	}
	return render(req, "posts/detail.html", context)

def posts_update(req, id=None):

	whiskey = get_object_or_404(Post, id=id)

# "initial" is a attribute of a form set?
	# update_form = PostForm(initial = {
	# 	"brand": whiskey.brand, 
	# 	"brand_type": whiskey.brand_type,
	# 	"price" : whiskey.price,
	# 	"description": whiskey.description
	# 	})
# instance = whiskey is something learned from Jeff
	update_form = PostForm(req.POST or None, instance = whiskey)
	print(update_form)
	if update_form.is_valid():
		instance = update_form.save()
		# instance.save()
		return redirect(instance)
	context = {
		"whiskey": update_form,
	}

	# PostForm(data=request.POST)
	return render(req, "posts/update.html", context)





