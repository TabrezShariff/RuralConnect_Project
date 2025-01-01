from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/order/', views.create_order, name='create_order'),
    path('order/<int:order_id>/summary/', views.order_summary, name='order_summary'),
]

