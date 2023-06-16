from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from apps.usuario_custom.models import Usuario


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
                    new_custom_user = Usuario.objects.create(
                        user=new_user,
                        imagen_perfil=profile_image,
                        fecha_nacimiento=birthdate
                    )
                    return redirect("signin")
                
                return render(request, 'auth/signup.html', {'message': 'La contraseña debe ser mayor o igual a 8 caracteres.'})
            return render(request, 'auth/signup.html', {'message': 'Error: las contraseñas no coinciden.'})
        return render(request, 'auth/signup.html', {'message': 'Error: ya existe un usuario con ese username.'})

    return render(request, "auth/signup.html")


def signin(request):
    if request.user.is_authenticated:
        return redirect('usuario')
    
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


def server_error(request):
    return render(request, '500.html')


def page_not_found_error(request, exception):
    return render(request, '404.html')


def permission_denied_error(request, exception):
    return render(request, '403.html')
