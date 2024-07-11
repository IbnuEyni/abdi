from django.shortcuts import render

from .models import Dentist, DentTitle

# Create your views here.
def doctors(requests):
    dentists = Dentist.objects.all()
    docTitle = DentTitle.objects.all()

    res = {
        'dentists':dentists, 
        'docTitle':docTitle
        }

    return render(requests, "doctors.html", res)