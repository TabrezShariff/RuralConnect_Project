# logistics/models.py
from django.db import models

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    order_id = models.CharField(max_length=100, unique=True)
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery {self.order_id} - {self.status}"

    class Meta:
        verbose_name_plural = "Deliveries"