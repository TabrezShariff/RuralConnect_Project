# logistics/urls.py
from django.urls import path
from . import views

app_name = 'logistics'

urlpatterns = [
    path('', views.delivery_list, name='delivery_list'),
    path('create/', views.create_delivery, name='create_delivery'),
    path('<int:pk>/', views.delivery_detail, name='delivery_detail'),
]