from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader

# Create your views here.

def registrate(request: HttpRequest):
    template = loader.get_template("registration.html")
    context = {"name":"mate","message":"szia",}
    return HttpResponse(template.render(context))