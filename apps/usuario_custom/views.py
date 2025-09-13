import json
from django.shortcuts import render, redirect
from .form import UserForm
from .models import Usuario
from .utils import change_password, PasswordException


def usuario_index(request):
    if request.user.is_authenticated:
        user = request.user
        usuario_custom = Usuario.objects.filter(user__id=user.id).first()
        form_user = UserForm(instance=user)
        has_profile_image = bool(usuario_custom.imagen_perfil)
        if request.method == 'POST':
            try:
                change_password(request, user)
            except PasswordException as pe:
                context = {
                    'form': form_user,
                    'usuario': usuario_custom,
                    'messages': str(pe),
                    'has_profile_image': has_profile_image
                }
                return render(request, 'usuario.html', context)
            form_user = UserForm(request.POST, instance=user)
            if form_user.is_valid():
                form_user.save()
                success_message = 'Los cambios fueron realizados correctamente!'
                context = {
                    'form': form_user,
                    'usuario': usuario_custom,
                    'success_message': success_message,
                    'has_profile_image': has_profile_image
                }
                return render(request, 'usuario.html', context)
            else:
                messages_json = form_user.errors.as_json(escape_html=True)
                messages = json.loads(messages_json)['username'][0]['message']
                context = {
                    'form': form_user,
                    'usuario': usuario_custom,
                    'messages': messages,
                    'has_profile_image': has_profile_image
                }
                return render(request, 'usuario.html', context)
            
        context = {
            'form': form_user, 
            'usuario': usuario_custom,
            'has_profile_image': has_profile_image
        }
        return render(request, 'usuario.html', context)
    
    return redirect('signup')
