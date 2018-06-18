from django.shortcuts import render
from myapp.models import *
from myapp.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from django.db.models import Q
from rest_framework.views import APIView
#from rest_framework import AuthView
from rest_framework.utils.urls import replace_query_param

#This is Program API
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    
class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer