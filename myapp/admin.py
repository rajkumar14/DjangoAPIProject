# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Article)