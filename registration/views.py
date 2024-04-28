from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from home.appforms import  RegisterForm, LoginForm
# Create your views here.
 

def registrate(request: HttpRequest):
    if request.method == 'GET':
        template = loader.get_template("registration.html")
        context = {"form":RegisterForm(),}
        return HttpResponse(template.render(context,request=request))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            user: User = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('hello')
        else:
            return redirect('hello')
        
def signin(request: HttpRequest):
    if(request.method == 'GET'):
        template = loader.get_template("login.html")
        context = {"form":LoginForm(),"errors":[]}
        return HttpResponse(template.render(context,request))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('hello')
            else:      
                template = loader.get_template("login.html")
                context = {"form": LoginForm,"errors":["Wrong username or Password"]}
                return HttpResponse(template.render(context,request))

def signout(request: HttpRequest):
    logout(request)
    return redirect('hello')