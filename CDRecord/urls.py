from django.urls import path
from . import views

urlpatterns = [
    path('myrecords/', views.addremove, name="my records"),
    path('addCategory/',views.addCategory,name="Add category"),
    path('removecat/<str:name>',views.removeCat, name = "remove category")
]