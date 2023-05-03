import json
from django.shortcuts import render, redirect
from .form import UserForm
from .models import Usuario


def usuario_index(request):
    if request.user.is_authenticated:
        user = request.user
        usuario_custom = Usuario.objects.filter(user__id=user.id).first()
        form_user = UserForm(instance=user)
        profile_image = True if usuario_custom.imagen_perfil else False
        if request.method == 'POST':
            password = request.POST['password']
            if user.check_password(password):
                form_user = UserForm(request.POST, instance=user)
                if form_user.is_valid():
                    form_user.save()
                    success_message = 'Los cambios fueron realizados correctamente!'
                    context = {
                        'form': form_user,
                        'usuario': usuario_custom,
                        'success_message': success_message,
                        'profile_image': profile_image
                    }
                    return render(request, 'usuario.html', context)
                else:
                    messages_json = form_user.errors.as_json(escape_html=True)
                    messages = json.loads(messages_json)['username'][0]['message']
                    context = {
                        'form': form_user,
                        'usuario': usuario_custom,
                        'messages': messages,
                        'profile_image': profile_image
                    }
                    return render(request, 'usuario.html', context)
            else:
                messages = 'La contraseña introducida no es correcta'
                context = {
                    'form': form_user,
                    'usuario': usuario_custom,
                    'messages': messages,
                    'profile_image': profile_image
                }
                return render(request, 'usuario.html', context)
        context = {
            'form': form_user, 
            'usuario': usuario_custom,
            'profile_image': profile_image
        }
        return render(request, 'usuario.html', context)

    return redirect('signup')
