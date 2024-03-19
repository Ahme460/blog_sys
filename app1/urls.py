from django.urls import path,include
from . import  views

urlpatterns = [

    path('register/',views.register,name='register'),
    path('log/',views.log,name='log'),
    path('home/',views.home,name='home'),
]
 