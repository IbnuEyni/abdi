from django.shortcuts import render

from .models import Services, Smile

# Create your views here.

import logging

logger = logging.getLogger(__name__)

def service(request):
    servs = Services.objects.all()
    smiles = Smile.objects.all()
    logger.info(f"Services: {servs}")
    logger.info(f"Smiles: {smiles}")
    return render(request, "services.html", {"servs": servs, "smiles": smiles})
