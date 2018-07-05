# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.http import 
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import csv
import codecs 
# Create your views here.
def Homepage(request):
	return render(request,'home.html')

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
	artical = Article.objects.all().order_by('-id')
	paginator = Paginator(artical, 5)
	page = request.GET.get('page')
	try:
		artical = paginator.page(page)
	except PageNotAnInteger:
		artical = paginator.page(1)
	except EmptyPage:
		artical = paginator.page(paginator.num_pages)
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

def ViewPage(request,pk):
	author = Author.objects.all()
	article = Article.objects.get(id=pk)
	return render(request,'view_datails.html',locals())

#Export csv
def export_aritcaldata(request):
    import csv
    from django.utils.encoding import smart_str
    dt = datetime.datetime.now()
    csv_name = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="'+ 'Raj' + "-" + csv_name +'.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),smart_str(u"Title"),smart_str(u"Content"),smart_str(u"Author") ])
    queryset = Article.objects.all()
    for obj in queryset:
            writer.writerow([
            smart_str(obj.id),
            smart_str(obj.title),
            smart_str(obj.content),
            smart_str(obj.author),
        ])
    return response

# Import CSV
def upload_csv(request):
	if request.method == "POST":
		f = request.FILES['csv_file']
        reader = csv.reader(f)
        keys = reader.next()
        for count, row in enumerate(reader):
			data = dict(zip(keys,row))
			try:
				obj = Article.objects.create(title= data.get('Title'),contentr=data.get('Content'),author=data.get('Author'))
				msg = "Data for  Added was successfully saved  ."
			except:
				msg = " Data for added uploaded partially ."
	return render(request, "upload_csv.html", locals())

    