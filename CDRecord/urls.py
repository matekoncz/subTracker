from django.urls import path
from . import views

urlpatterns = [
    path('myrecords/', views.addremove, name="my records"),
    path('addCategory/',views.addCategory,name="Add category"),
    path('removecat/<str:name>',views.removeCat, name = "remove category"),
    path('addsubscription/',views.addSubscription,name="Add subscription"),
    path('removesub/<str:name>',views.removeSub, name = "remove subscription")
]