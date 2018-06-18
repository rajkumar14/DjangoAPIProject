# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.http import 
from django.contrib.auth.decorators import login_required
from myapp.models import *

# Create your views here.

def Login(request):

	if request.method =="POST":
		username = request.POST.get("email")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
		    login(request, user)
		    message="Successfully login"
		    return HttpResponseRedirect('/list/')
		    # A backend authenticated the credentials
		else:
			message = "Invalid Username and password"
		    # No backend authenticated the credentials
	return render(request,'login.html')

def Logout(request):
    logout(request)
    # return HttpResponseRedirect('/login/')
    # Redirect to a success page.

@login_required(login_url='/login/')
def Home(request):
	return render(request,'raj.html')

def ListPage(request):
	artical = Article.objects.all()
	return render(request,'list.html',locals())

def AddPage(request):
	author = Author.objects.all()
	if request.method == "POST":
		# import ipdb;ipdb.set_trace();
		title = request.POST.get('title')
		content = request.POST.get('content')
		auth = request.POST.get('author')
		auth1= Author.objects.get(id=auth)
		article = Article.objects.create(title=title,content=content,author=auth1)
		return HttpResponseRedirect('/list/')
		# article.author = author.auth
		# article.save()

	return render(request,'add.html',locals())


def EditPage(request,pk):
	author = Author.objects.all()
	article = Article.objects.get(id=pk)
	if request.method == "POST":
		# import ipdb;ipdb.set_trace();
		title = request.POST.get('title')
		content = request.POST.get('content')
		auth = request.POST.get('author')
		auth1= Author.objects.get(id=auth)
		article = Article.objects.get(id=pk)
		article.title=title
		article.content=content
		article.author=auth1
		article.save()
		return HttpResponseRedirect('/list/')
	return render(request,'edit.html',locals())