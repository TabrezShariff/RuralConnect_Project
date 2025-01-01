from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('marketplace:product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/create_product.html', {'form': form})

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.buyer = request.user
            order.product = product
            order.total_price = product.price * order.quantity
            order.save()
            return redirect('marketplace:order_summary', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'marketplace/order_form.html', {'form': form, 'product': product})

def order_summary(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'marketplace/order_summary.html', {'order': order})

