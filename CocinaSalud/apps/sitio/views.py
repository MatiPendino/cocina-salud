from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def acerca_de(request):
    return render(request, "acerca_de.html")


def signup(request):

    users = User.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        username_repeated = True if User.objects.filter(username=username).first() else False

        if not username_repeated:
            if pass1 == pass2:
                if len(pass1) >= 8:
                    new_user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=pass1,
                        first_name=first_name,
                        last_name=last_name
                    )
                    new_user.save()
                    return redirect("signin")
                
                return render(request, 'auth/signup.html', {'message': 'La contraseña debe ser mayor o igual a 8 caracteres.'})
            return render(request, 'auth/signup.html', {'message': 'Error: las contraseñas no coinciden.'})
        return render(request, 'auth/signup.html', {'message': 'Error: ya existe un usuario con ese username.'})

    return render(request, "auth/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'auth/signin.html', {'message': 'Su correo y/o su contraseña son incorrectas.'})

    return render(request, "auth/signin.html", {})


def sign_out(request):
    logout(request)
    return redirect("/")

# TODO: crear mensajes de error 404 y 500 personalizados