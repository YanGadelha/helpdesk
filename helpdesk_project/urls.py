from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from helpdesk import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
]