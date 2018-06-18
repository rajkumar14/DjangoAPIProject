from rest_framework import serializers
from myapp.models import *
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =('id','name','email','mobile','address')