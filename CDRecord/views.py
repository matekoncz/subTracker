from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from home.models import Cathegory, Subscription

# Create your views here.

def addremove(request: HttpRequest):
    if request.method =='GET':
        template = loader.get_template('addremove.html')
        context = {'categories': Cathegory.objects.filter(user=request.user.id)}
        return HttpResponse(template.render(request=request,context=context))