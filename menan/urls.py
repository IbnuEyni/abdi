from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

# app_name = 'menan'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('appointment/', views.make_appointment, name='appointment'),
    path('subscribe/', views.subscribe, name='subscribe')
    # path('blog.html', views.blog, name='blog'),
    # path('menan/<int:pk>/', views.blog_detail, name='blog_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
