from django.shortcuts import render

from .models import Services, Smile
from menan.models import Slider, Contact
from blog.models import Blog
from doctor.models import Achievements, Pricing, PriTitle

# Create your views here.

import logging

logger = logging.getLogger(__name__)

def services(request):
    slider = Slider.objects.all()
    sliders = slider[:1]
    servs = Services.objects.all()
    achievs = Achievements.objects.all()
    pritits = PriTitle.objects.all()
    pricings = Pricing.objects.all()
    smiles = Smile.objects.all()  
    logger.info(f"Services: {servs}")
    logger.info(f"Smiles: {smiles}")
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]

    context = {"servs": servs, 
               "smiles": smiles, 
               "sliders":sliders, 
               "contacts":contacts, 
               "blgs":blgs,
               "pricings":pricings,
               "pritits":pritits,
               "achievs":achievs,
               }
    return render(request, "services.html", context)
