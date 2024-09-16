from django.urls import path

from account import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logOut, name='logout'),
    path('user/', views.userPage, name='user')
]  