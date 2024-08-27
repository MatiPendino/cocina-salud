from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from apps.base.utils import PasswordException
from .utils import create_custom_user


def signup(request):
    if request.user.is_authenticated:
        return redirect('usuario')
    
    if request.method == "POST":
        birthdate = request.POST['birthdate']
        try:
            profile_image = request.FILES['profile_image']
        except:
            profile_image = None
        username = request.POST['username']
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        try:
            create_custom_user(
                pass1, pass2, username, first_name, last_name, email,
                birthdate, profile_image
            )
            return redirect('signin')
        except PasswordException as pe:
            return render(request, 'auth/signup.html', {'message': pe})
        
    return render(request, 'auth/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('usuario')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auth/signin.html', {'message': 'Su correo y/o su contraseña son incorrectas.'})

    return render(request, "auth/signin.html", {})


def sign_out(request):
    logout(request)
    return redirect("/")


def server_error(request):
    return render(request, '500.html')


def page_not_found_error(request, exception):
    return render(request, '404.html')


def permission_denied_error(request, exception):
    return render(request, '403.html')
