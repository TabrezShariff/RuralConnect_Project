# logistics/forms.py
from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['order_id', 'pickup_address', 'delivery_address']