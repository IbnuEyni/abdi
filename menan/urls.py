from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('doctors', views.doctors, name='doctors'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
