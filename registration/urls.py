from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrate, name="registrate"),
    path('login/',views.signin,name="log in")
]