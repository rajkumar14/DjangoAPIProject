# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=100,blank=True,null=True)
	content = models.CharField(max_length=200,blank=True,null=True)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.title

class Student(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	email = models.CharField(max_length=100,blank=True,null=True)
	mobile = models.CharField(max_length=100,blank=True,null=True)
	address = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.name