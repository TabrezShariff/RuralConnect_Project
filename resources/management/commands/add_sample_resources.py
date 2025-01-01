from django.core.management.base import BaseCommand
from resources.models import Resource
from django.utils import timezone
from django.core.files import File
from django.conf import settings
import os
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Adds sample resources to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to add sample resources...'))
        
        resources = [
            {
                'title': 'Sustainable Rice Intensification',
                'description': 'Learn about SRI, an innovative method to increase rice yields while reducing water usage.',
                'category': 'CROP_MANAGEMENT',
                'content': 'Sustainable Rice Intensification (SRI) is a climate-smart, agroecological methodology for increasing the productivity of rice and more recently other crops by changing the management of plants, soil, water and nutrients...',
                'source': 'Indian Council of Agricultural Research (ICAR)',
                'source_url': 'https://icar.gov.in/content/sustainable-rice-intensification-sri',
                'publication_date': timezone.now().date(),
                'preview_image': 'img01.jpg',
            },
            {
                'title': 'Soil Health Card Scheme',
                'description': 'Understanding and utilizing the Soil Health Card scheme for better crop management.',
                'category': 'SOIL_HEALTH',
                'content': 'The Soil Health Card scheme is a flagship program launched by the Government of India to assess the nutrient status of every farmland in the country...',
                'source': 'Ministry of Agriculture & Farmers Welfare',
                'source_url': 'https://www.soilhealth.dac.gov.in/',
                'publication_date': timezone.now().date(),
                'preview_image': 'img02.jpg',
            },
            {
                'title': 'Pradhan Mantri Krishi Sinchayee Yojana',
                'description': 'Exploring the benefits and implementation of the PMKSY for efficient water management.',
                'category': 'WATER_MANAGEMENT',
                'content': 'The Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) is a national mission to improve farm productivity and ensure better utilization of water resources...',
                'source': 'Ministry of Jal Shakti',
                'source_url': 'http://pmksy.gov.in/',
                'publication_date': timezone.now().date(),
                'preview_image': 'img03.jpg',
            },
            {
                'title': 'Integrated Pest Management in Cotton',
                'description': 'Effective strategies for managing pests in cotton cultivation using IPM techniques.',
                'category': 'PEST_CONTROL',
                'content': 'Integrated Pest Management (IPM) in cotton involves a combination of cultural, biological, and chemical methods to control pests while minimizing environmental impact...',
                'source': 'Central Institute for Cotton Research',
                'source_url': 'https://www.cicr.org.in/ipm.html',
                'publication_date': timezone.now().date(),
                'preview_image': 'img04.jpg',
            },
            {
                'title': 'Export Opportunities for Indian Spices',
                'description': 'Exploring international markets and trends for Indian spice exports.',
                'category': 'MARKET_TRENDS',
                'content': "India is the world's largest producer, consumer, and exporter of spices. This resource explores current market trends, quality standards, and export procedures for Indian spices...",
                'source': 'Spices Board India',
                'source_url': 'http://www.indianspices.com/export-opportunities',
                'publication_date': timezone.now().date(),
                'preview_image': 'img05.jpg',
            },
            {
                'title': 'PM-KISAN Scheme Benefits',
                'description': 'Understanding the Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) scheme and its benefits for farmers.',
                'category': 'GOVERNMENT_SCHEMES',
                'content': 'The PM-KISAN scheme aims to provide income support to all landholding farmer families in the country. This resource explains eligibility criteria, benefits, and the application process...',
                'source': 'Ministry of Agriculture & Farmers Welfare',
                'source_url': 'https://pmkisan.gov.in/',
                'publication_date': timezone.now().date(),
                'preview_image': 'img06.jpg',
            },
        ]

        try:
            # Clear existing resources
            Resource.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing resources'))

            for resource_data in resources:
                preview_image = resource_data.pop('preview_image')
                resource = Resource.objects.create(**resource_data)
                
                # Add preview image
                image_path = os.path.join(settings.BASE_DIR, 'resources', 'sample_images', preview_image)
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as img_file:
                        resource.preview_image.save(preview_image, File(img_file), save=True)
                else:
                    logger.warning(f"Image file not found: {image_path}")

                self.stdout.write(self.style.SUCCESS(f'Added resource: {resource.title}'))

            self.stdout.write(self.style.SUCCESS('Successfully added all sample resources'))
            
            # Print final count
            count = Resource.objects.count()
            self.stdout.write(self.style.SUCCESS(f'Total resources in database: {count}'))

        except Exception as e:
            logger.error(f"Error adding resources: {str(e)}")
            self.stdout.write(self.style.ERROR(f'Error adding resources: {str(e)}'))

