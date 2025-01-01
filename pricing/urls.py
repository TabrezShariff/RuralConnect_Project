# pricing/urls.py
from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.price_list, name='price_list'),
    
]