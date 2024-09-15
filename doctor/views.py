from django.shortcuts import get_object_or_404, render

from .models import Dentist, DentTitle, Pricing, PriTitle, Achievements
from menan.models import Contact, Slider, Abt_Presonal
from blog.models import Blog
from doctor.models import Dentist

# Create your views here.
def doctors(requests):
    slider = Slider.objects.all()
    sliders = slider[:1]
    dentists = Dentist.objects.all()
    docTitle = DentTitle.objects.all()
    pricings = Pricing.objects.all()
    pritits = PriTitle.objects.all()
    achievs = Achievements.objects.all() 
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]

    res = {
        'dentists':dentists, 
        'docTitle':docTitle,
        'pricings':pricings,
        'pritits':pritits,
        'achievs':achievs,
        'sliders': sliders,
        'contacts':contacts,
        'blgs':blgs,
        }

    return render(requests, "doctors.html", res)

def doctor_detail(request, pk):
    slider = Slider.objects.all()
    sliders = slider[:1]
    dentists = Dentist.objects.all()
    persons = Abt_Presonal.objects.all()
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]
    if request.method == 'GET':
        blog = get_object_or_404(Blog, pk=pk)
        context = {
            'blog':blog,
            'sliders':sliders,
            'contacts':contacts,
            'blgs':blgs,
            'dentists':dentists,
            'persons':persons,
            }
        return render(request, 'doctor-single.html', context)