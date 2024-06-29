from django.shortcuts import render
from django.core.mail import send_mail
from .models import Dentist, Testimonials

def home(requests):
    dents = Dentist.objects.all()
    tests = Testimonials.objects.all()
    # dent1 = Dentist()
    # dent1.name = "Tom Smith"
    # dent1.prof = "Dentist"
    # dent1.desc = "Far far away, behind the word mountains, far from the countries Vokalia"

    # dent2 = Dentist()
    # dent2.name = "Mark Wilson"
    # dent2.prof = "Dentist"
    # dent2.desc = "Far far away, behind the word mountains, far from the countries Vokalia"

    # dent3 = Dentist()
    # dent3.name = "Patrick Jacobson"
    # dent3.prof = "Dentist"
    # dent3.desc = "Far far away, behind the word mountains, far from the countries Vokalia"

    # dent4 = Dentist()
    # dent4.name = "Ivan Dorchsner"
    # dent4.prof = "System Analyst"
    # dent4.desc = "Far far away, behind the word mountains, far from the countries Vokalia"

    # dents = [dent1, dent2, dent3, dent4]

    return render(requests, 'index.html', {'dents': dents, 'tests': tests})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        umessage = request.POST['umessage']

        send_mail(
            message_name, #User name
            message_subject, # Message Subject
            umessage, # Messages
            message_email, # from email
            ['mirahaem5@gmail.com'], # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def services(request):
    return render(request, 'services.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})