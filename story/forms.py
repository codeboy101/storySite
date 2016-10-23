from django import forms
from .models import Story

class PostForm(forms.ModelForm):

	class Meta:
		model = Story
		fields = ('title','body',)

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30)	
	password = forms.CharField(widget=forms.PasswordInput())

class CreateForm(forms.Form):
	
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=254)	
	password = forms.CharField(widget=forms.PasswordInput())
