from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import *
from blog.models import Blog


def home(requests):
    sliders = Slider.objects.all()
    dents = Dentist.objects.all()
    tests = Testimonials.objects.all()
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]
    # dent1 = Dentist()
    # dent1.name = "Tom Smith"
    # dent1.prof = "Dentist"
    # dent1.desc = "Far far away, behind the word mountains, far from the countries Vokalia"
    # dents = [dent1, dent2, dent3, dent4]

    return render(requests, 'index.html', {'dents': dents, 'tests': tests, 'sliders':sliders, 'blgs':blgs, 'contacts':contacts})

def contact(request):
    slider = Slider.objects.all()
    sliderss = slider[:1]
    contacts = Contact.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]

    if request.method == 'POST':
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message_subject = request.POST.get('message-subject')
        umessage = request.POST.get('umessage')

        try:
            send_mail(
                message_subject, # Email subject
                umessage, # Email message
                message_email, # From email
                ['readshare192@gmail.com'], # To email  
                fail_silently=False,
            )
            return render(request, 'contact.html', {'sliderss': sliderss, 'contacts': contacts, 'message_name': message_name, 'success': True, 'blgs':blgs})
        except Exception as e:
            return render(request, 'contact.html', {'sliderss': sliderss, 'contacts':contacts, 'message_name': message_name, 'error': str(e), 'blgs':blgs})
    else:
        return render(request, 'contact.html', {'sliderss': sliderss, 'contacts':contacts, 'blgs':blgs})
def about(request):
    slider = Slider.objects.all()
    sliders = slider[:1]
    mission = Our_mission.objects.all()
    goal = Our_goal.objects.all()
    action = What_we_do.objects.all()
    persons = Abt_Presonal.objects.all()
    blg = Blog.objects.all()
    blgs = blg[:2]
    contacts = Contact.objects.all()
    res = {
        "missions":mission,
        "goals": goal,
        "actions":action,
        "persons":persons,
        "sliders":sliders,
        'blgs':blgs, 
        'contacts':contacts

    }
    return render(request, 'about.html', res)



