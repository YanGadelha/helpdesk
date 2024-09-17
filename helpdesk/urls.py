from django.urls import path
from . import views
#tai meu patrao, o que mais?
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('update/<int:pk>/', views.update_ticket, name='update_ticket'),
    path('delete/<int:pk>/', views.delete_ticket, name='delete_ticket'),
]
