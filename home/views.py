from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    template = loader.get_template("homeTemplate.html")
    return HttpResponse(template.render())
