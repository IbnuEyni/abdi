from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm, AuthenticateUserForm
from .decorators import  allowed_users, authenticated_user


# Create your views here.
@authenticated_user
def registerPage(request):
   
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + username)
    
            return redirect('login')
    
    contex = {'form':form}
    return render(request, 'registration.html', contex)

@authenticated_user
def loginPage(request):
   
    form  = AuthenticateUserForm()

    if request.method == 'POST':
            form = AuthenticateUserForm(request.POST)
            if form.is_valid:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"welcome back, {username}!")
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')

    contex = {'form':form}
    return render(request, 'login.html', contex)

def logOut(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
# # @allowed_users(allowed_roles=['customers'])
# def homePage(request):
#     context = {}
#     return render(request, 'index.html', context)

@login_required(login_url='login')
# @admin_only
def userPage(request):
    context = {}
    return render(request, 'index.html', context)