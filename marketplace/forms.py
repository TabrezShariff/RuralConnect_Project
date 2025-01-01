from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'shipping_address']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 3}),
        }

