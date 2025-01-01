from django.shortcuts import render
from .models import Resource
import logging


logger = logging.getLogger(__name__)

def resource_list(request):
    try:
        resources = Resource.objects.all().order_by('-publication_date')
        logger.info(f"Number of resources found: {resources.count()}")
        
        # Print each resource for debugging
        for resource in resources:
            logger.info(f"Resource: {resource.title}")
        
        return render(request, 'resources/resource_list.html', {'resources': resources})
    except Exception as e:
        logger.error(f"Error fetching resources: {str(e)}", exc_info=True)
        return render(request, 'resources/resource_list.html', {'error': str(e)})

