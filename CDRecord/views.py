from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import Context, Template, loader
from home.models import Category, Subscription
from home.appforms import CategoryForm, SubscriptionForm


# Create your views here.

def addremove(request: HttpRequest):
    if request.method =='GET':
        template = loader.get_template('addremove.html')
        cats = Category.objects.filter(user=request.user.id)
        catnum={}
        for cat in cats:
            catnum[cat.name] = Subscription.objects.filter(category=get_object_or_404(Category,name=cat.name,user=request.user.id)).count()
        context = {
                    'categories': cats,
                    'categoryform':CategoryForm(),
                    'subscriptions':Subscription.objects.filter(user=request.user.id),
                    'subscriptionform':SubscriptionForm(user=request.user),
                    'catnum':catnum
                   }
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
        
def removeCat(request: HttpRequest,name):
    category = get_object_or_404(Category,name=name,user=request.user)
    category.delete()
    return redirect('my records')

def addSubscription(request: HttpRequest):
    form = SubscriptionForm(data=request.POST,user=request.user)
    if(form.is_valid()):
        sub = Subscription(service_name=form.cleaned_data['service_name'],price=form.cleaned_data['price'],user=request.user,category=get_object_or_404(Category,name = form.cleaned_data['category'],user=request.user))
        try:
            sub.save()
            return redirect('my records')
        except Exception as e:
            return redirect(e.msg)
        
def removeSub(request: HttpRequest,name):
    sub = get_object_or_404(Subscription,service_name=name,user=request.user)
    sub.delete()
    return redirect('my records')