from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0]

            if str(group) in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Your not Authorized to access this page')
        return wrapper_func
    return decorator

# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0]

#         if str(group) == 'customers':
#             return redirect('user')
        
#         if str(group) == 'admin':
#             return view_func(request, *args, **kwargs)
#     return wrapper_func
