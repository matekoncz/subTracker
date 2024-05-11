from django.urls import path
from . import views

urlpatterns = [
    path("",views.redirect_to_hello, name="redirect"),
    path("hello/", views.hello, name="hello"),
]
