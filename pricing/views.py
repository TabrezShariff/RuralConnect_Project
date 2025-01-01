from django.shortcuts import render
from django.utils import timezone
import random

def price_list(request):
    # Dummy data for price updates
    products = [
        "Rice", "Wheat", "Maize", "Soybeans", "Potatoes",
        "Tomatoes", "Onions", "Apples", "Mangoes", "Milk"
    ]
    
    price_updates = []
    for product in products:
        price = round(random.uniform(20, 200), 2)  # Random price between ₹20 and ₹200
        change = round(random.uniform(-5, 5), 2)   # Random change between -₹5 and ₹5
        price_updates.append({
            'product': product,
            'price': price,
            'change': change
        })
    
    context = {
        'price_updates': price_updates,
        'last_updated': timezone.now()
    }
    return render(request, 'pricing/pricing_list.html', context)

