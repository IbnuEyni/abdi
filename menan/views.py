import os
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from clinic import settings
from service.models import Services
from doctor.models import Achievements, Pricing, PriTitle
from .models import *
from blog.models import Blog


def home(requests):
    sliders = Slider.objects.all()
    dents = Dentist.objects.all()
    tests = Testimonials.objects.all()
    contacts = Contact.objects.all()
    servs = Services.objects.all()
    persons = Abt_Presonal.objects.all()
    achievs = Achievements.objects.all() 
    pricings = Pricing.objects.all()
    pritits = PriTitle.objects.all()
    blg = Blog.objects.all()
    blogs = blg[:4]
    blgs = blg[:2]
    sliderss = sliders[:1]

    context = {'dents': dents, 
               'tests': tests, 
               'sliders':sliders, 
               'blgs':blgs, 
               'blogs':blogs,
               'contacts':contacts, 
               'servs':servs, 
               'persons':persons,
               'pricings':pricings, 
               'pritits':pritits,
               'achievs':achievs,
               'sliderss':sliderss,
               }

    return render(requests, 'index.html', context)

def contact(request):
    slider = Slider.objects.all()
    sliderss = slider[:1]
    contacts = Contact.objects.all()
    map_settings = MapSettings.objects.first()  
    map_url = map_settings.map_url if map_settings else "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.1637489996847!2d38.7352157744991!3d9.048823788679371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x164b8f74e36f9e2d%3A0xe052c08008eb85a6!2zRW5rdWxhbCBGYWJyaWNhIFNxdWFyZSB8IOGKpeGKleGJgeGIi-GIjSDhjYvhiaXhiKrhiqsg4Yqg4Yuw4Ymj4Ymj4Yut!5e0!3m2!1sen!2set!4v1704783423949!5m2!1sen!2set"
    blg = Blog.objects.all()
    blgs = blg[:2]

    if request.method == 'POST':
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message_subject = request.POST.get('message-subject')
        umessage = request.POST.get('umessage')

        # Construct the full message
        full_message = (
            f"Name: {message_name}\n"
            f"Email: {message_email}\n\n"
            f"Message:\n{umessage}"
        )

        try:
            send_mail(
                subject=message_subject,           # Email subject
                message=full_message,              # Email message
                from_email=message_email,  # From email (must be your email)
                recipient_list=['readshare192@gmail.com'],  # To email
                fail_silently=False,
            )
            return render(request, 'contact.html', {
                'sliderss': sliderss,
                'contacts': contacts,
                'map_url': map_url,
                'message_name': message_name,
                'success': True,
                'blgs': blgs
            })
        except Exception as e:
            error_message = f"An error occurred: {e}"
            return render(request, 'contact.html', {
                'sliderss': sliderss,
                'contacts': contacts,
                'map_url': map_url,
                'message_name': message_name,
                'error': error_message,
                'blgs': blgs
            })
    else:
        return render(request, 'contact.html', {
            'sliderss': sliderss,
            'contacts': contacts,
            'map_url': map_url,
            'blgs': blgs
        })
    
def about(request):
    slider = Slider.objects.all()
    sliders = slider[:1]
    mission = Our_mission.objects.all()
    goal = Our_goal.objects.all()
    action = What_we_do.objects.all()
    persons = Abt_Presonal.objects.all()
    tests = Testimonials.objects.all()
    achievs = Achievements.objects.all() 
    blg = Blog.objects.all()
    blgs = blg[:2]
    contacts = Contact.objects.all()
    res = {
        "missions":mission,
        "goals": goal, 
        "actions":action,
        "persons":persons,
        "tests":tests,
        "achievs":achievs,
        "sliders":sliders,
        'blgs':blgs, 
        'contacts':contacts

    }
    return render(request, 'about.html', res)

def make_appointment(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        appointment_date = request.POST.get('appointment_date')

        # Check for required fields
        if not all([department, name, email, phone, appointment_date]):
            return render(request, 'index.html', {
                'success_message': None,
                'error_message': 'All required fields must be filled out.'
            })

        try:
            # Save the appointment details to the database
            # Appointments.objects.create(
            #     department=department,
            #     name=name,
            #     email=email,
            #     phone=phone,
            #     appointment_date=appointment_date
            # )

            # Construct and send the email
            full_message = (
                f"Appointment Details:\n\n"
                f"Department: {department}\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Appointment Date: {appointment_date}\n"
            )
            send_mail(
                subject=f"New Appointment from {name}",
                message=full_message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return render(request, 'index.html', {
                'success_message': f"Thank you, {name}. Your appointment has been made successfully.",
                'error_message': None
            })
        except Exception as e:
            return render(request, 'index.html', {
                'success_message': None,
                'error_message': f"An error occurred: {e}"
            })
    else:
        return redirect('home')