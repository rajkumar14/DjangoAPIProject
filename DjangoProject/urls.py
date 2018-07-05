"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from myapp.feeds_views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Homepage, name='homepage'),
    url(r'^login/$',Login,name='login'),
    url(r'^logout/$',Logout,name='logout'),    
    url(r'^page/$',Home,name='page'),
    url(r'^list/$',ListPage,name='list'),
    url(r'^add-artical/$',AddPage,name='add-artical'),
    url(r'^edit-artical/(?P<pk>\d+)/$',EditPage,name='edit_artical'),
    url(r'^view-deatils/(?P<pk>\d+)/$',ViewPage,name='view_deatils'),
    url(r'^student/$', StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$', StudentDetails.as_view()),
    url(r'^csv-download/$',export_aritcaldata,name='csv_download'),
    url(r'^upload_csv/$', upload_csv, name='upload_csv'),
]
