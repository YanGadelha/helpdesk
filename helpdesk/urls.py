from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('delete_user/', views.delete_user_view, name='delete_user'),
    path('user_profile/', views.user_profile_view, name='user_profile'),
    path('add_order/', views.add_order, name='add_order'),
    path('all-orders/', views.all_orders_view, name='all_orders'), 
]