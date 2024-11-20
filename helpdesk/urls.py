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
    path('user_orders/', views.user_orders_view, name='user_orders'), 
    path('adicionar_comentario/<int:ordem_id>/', views.adicionar_comentario, name='adicionar_comentario'),
    path('atualizar_ordem/<int:ordem_id>/', views.atualizar_ordem, name='atualizar_ordem'),
    path('concluir_ordem/<int:ordem_id>/', views.concluir_ordem, name='concluir_ordem'),
    path('cancelar_ordem/<int:ordem_id>/', views.cancelar_ordem, name='cancelar_ordem'),
    path('excluir_ordem/<int:ordem_id>/', views.excluir_ordem, name='excluir_ordem'),
]