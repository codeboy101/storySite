from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse

def front(request):
	return render(request,"welcome/front.html")

def storyRedirect(request):
	return redirect('frontPage')
	