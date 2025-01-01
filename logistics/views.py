# logistics/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Delivery
from .forms import DeliveryForm

def delivery_list(request):
    deliveries = Delivery.objects.all().order_by('-created_at')
    return render(request, 'logistics/delivery_list.html', {'deliveries': deliveries})

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save()
            messages.success(request, 'Delivery request created successfully!')
            return redirect('logistics:delivery_detail', pk=delivery.pk)
    else:
        form = DeliveryForm()
    return render(request, 'logistics/delivery_form.html', {'form': form})

def delivery_detail(request, pk):
    delivery = Delivery.objects.get(pk=pk)
    return render(request, 'logistics/delivery_detail.html', {'delivery': delivery})