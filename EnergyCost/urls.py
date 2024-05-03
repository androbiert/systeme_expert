from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('Form_Process',views.PageProcess, name='input_process')
]