from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Story , Vote
from .forms import PostForm , LoginForm , CreateForm

def postStory(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"]
			body = form.cleaned_data["body"]
			print(type(title))
			s = Story.objects.create(title=title,body=body,author=str(request.user))
			s.save()
			user_instance = User.objects.get(username=request.user)
			v = Vote.objects.create(story=s,voter=user_instance)
			v.save()
			lista = len(Vote.objects.all())
			print(lista)
			
			return redirect(frontPage)

	return render(request,"story/postStory.html",{'form':form})

def readStory(request,pk):
	story = Story.objects.get(pk=pk)
	rating = story.total_votes
	author = story.author
	pub_date = story.pub_date
	return render(request,"story/readStory.html",{'story':story,'rating':rating,'author':author,'pub_date':pub_date})

def frontPage(request):
	print(request.user)
	username = "guest"
	if request.user.is_authenticated():
		username = request.user
	posts = Story.objects.order_by('title')
	return render(request,"story/frontPage.html",{'posts':posts,"username":username})

@login_required(login_url="login")
def changeRating(request,pk,value):
	story = Story.objects.get(pk=pk)
	try:
		vote = Vote.objects.get(story=story,voter=request.user)
	except ObjectDoesNotExist as e:
		user_instance = User.objects.get(username=request.user)
		vote = Vote.objects.create(story=story,voter=user_instance)
		vote.save()

	value = int(value)

	if not vote.has_voted:
		print("you havent voted")
		story.total_votes += value
		vote.vote_cast = value
		vote.has_voted = True

	elif vote.has_voted:
		print("you have voted")	
		if vote.vote_cast == 1 and value == -1:
			print("applying value {}".format(value))
			story.total_votes += (value - 1)

		if vote.vote_cast == -1 and value == 1:
			print("applying value {}".format(value))
			story.total_votes += (value + 1)

		vote.has_voted = True
		vote.vote_cast = value

	story.save()
	vote.save()

	print("vote.has_voted is now {}".format(vote.has_voted))
	return redirect("readStory",pk=pk)

def login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			input_username = form.cleaned_data["username"]
			input_pass = form.cleaned_data["password"]
			try:
				user = authenticate(username=input_username,password=input_pass)
				if user is not None:
					auth_login(request,user)
					print("login")
					return redirect("frontPage")

				return redirect("register")
			
			except AttributeError as e:
				print(e)
				return render(request,"story/errLogin.html",{"error":str(e)})

	return render(request,"story/create_login.html",{"loginForm":form})

def register(request):
	form = CreateForm()
	if request.method == "POST":
		form = CreateForm(request.POST)
		if form.is_valid():
			input_username = form.cleaned_data["username"]
			input_mail = form.cleaned_data["email"]
			input_pass = form.cleaned_data["password"]
			
			try:
				create = User.objects.create_user(username=input_username,password=input_pass,email=input_mail)
				create.save()
				auth_login(request,create)
				return redirect("frontPage")

			except IntegrityError as e:
				error = "Username already exists"
				return render(request,"story/errLogin.html",{"error":error})	

	return render(request,"story/create_login.html",{"createForm":form})

def redirector(request):
	return redirect("frontPage")

def logout(request):
	auth_logout(request)
	return redirect("frontPage")

def deleteStory(request,pk):
	story = Story.objects.get(pk=pk)
	story.delete()
	return redirect("frontPage")