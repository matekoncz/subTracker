from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from home.models import Category, Subscription
from home.appforms import CategoryForm

# Create your views here.

def addremove(request: HttpRequest):
    if request.method =='GET':
        template = loader.get_template('addremove.html')
        context = {'categories': Category.objects.filter(user=request.user.id),'categoryform':CategoryForm()}
        return HttpResponse(template.render(request=request,context=context))
    
def addCategory(request: HttpRequest):
    form = CategoryForm(request.POST)
    if(form.is_valid()):
        category = Category(name=form.cleaned_data['name'],description=form.cleaned_data['description'],user=request.user)
        try:
            category.save()
            return redirect('my records')
        except Exception as e:
            return redirect(e.msg)