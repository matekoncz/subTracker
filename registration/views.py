from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# Create your views here.

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

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
