from django.db import models
from django.utils import timezone


class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('CROP_MANAGEMENT', 'Crop Management'),
        ('SOIL_HEALTH', 'Soil Health'),
        ('WATER_MANAGEMENT', 'Water Management'),
        ('PEST_CONTROL', 'Pest Control'),
        ('MARKET_TRENDS', 'Market Trends'),
        ('GOVERNMENT_SCHEMES', 'Government Schemes'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    preview_image =  models.ImageField(upload_to='resources\sample_images', null=True, blank=True)
    source = models.CharField(max_length=200)
    source_url = models.URLField(max_length=500)
    publication_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

