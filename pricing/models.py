# pricing/models.py
from django.db import models

class PriceUpdate(models.Model):
    product_name = models.CharField(max_length=200)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} - ${self.current_price}"

    def save(self, *args, **kwargs):
        if self.previous_price > 0:
            self.change_percentage = ((self.current_price - self.previous_price) / self.previous_price) * 100
        super().save(*args, **kwargs)