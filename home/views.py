
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm

def index(request):
    context={"variable":"this is sent"}
    return render(request,'index.html')
    #return HttpResponse("this is home page")
def about(request):
    context={}
    return render(request,'about.html',context) 
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        problem=request.POST.get("problem")
        contact=Contact(name=name,phone=phone,email=email,problem=problem,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    context={}
    return render(request,'contact.html',context)

def mainpage(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'mainpage.html')
         
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/mainpage")

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
 
def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')

				return redirect('/index')
			

		context = {'form':form}
		return render(request, 'register.html', context)
