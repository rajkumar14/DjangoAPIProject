from django import forms
from myapp.models import *

class ArticleForm(forms.ModelForm):

	class Meta:
		model= Article
		fields =['id','title']
