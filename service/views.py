from django.shortcuts import render

from .models import Services, Smile
from menan.models import Slider, Contact
from blog.models import Blog

# Create your views here.

import logging

logger = logging.getLogger(__name__)

def services(request):
    slider = Slider.objects.all()
    sliders = slider[:1]
    servs = Services.objects.all()
    smiles = Smile.objects.all()
    logger.info(f"Services: {servs}")
    logger.info(f"Smiles: {smiles}")
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]
    return render(request, "services.html", {"servs": servs, "smiles": smiles, "sliders":sliders, "contacts":contacts, "blgs":blgs})
