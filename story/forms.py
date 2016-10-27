from django import forms
from .models import Story

class PostForm(forms.ModelForm):

	class Meta:
		model = Story
		fields = ('title','body',)

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30)	
	password = forms.CharField(widget=forms.PasswordInput(),max_length=30)

class CreateForm(forms.Form):

	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=254)	
	password = forms.CharField(widget=forms.PasswordInput())

class ResetPassForm(forms.Form):
	old_pass = forms.CharField(widget=forms.PasswordInput(),max_length=30)
	new_pass = forms.CharField(widget=forms.PasswordInput(),max_length=30)
	confirm_new_pass = forms.CharField(widget=forms.PasswordInput(),max_length=30)