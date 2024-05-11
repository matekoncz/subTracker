from django.urls import path
from . import views

urlpatterns = [
    path("myrecords/", views.addremove, name="my records"),
    path("addCategory/", views.add_category, name="Add category"),
    path("removecat/<str:name>", views.remove_cat, name="remove category"),
    path("addsubscription/", views.add_subscription, name="Add subscription"),
    path("removesub/<str:name>", views.remove_sub, name="remove subscription"),
]
