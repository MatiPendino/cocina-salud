from apps.base.utils import PasswordException


def change_password(request, user):
    password = request.POST['current_password']
    new_password1 = request.POST['new_password1']
    new_password2 = request.POST['new_password2']
    if password:
        if user.check_password(password):
            if len(new_password1) >= 8:
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()
                else:
                    raise PasswordException('Las contraseñas no coinciden')
            else:
                raise PasswordException('La nueva contraseña debe ser mayor o igual a 8 caracteres')
        else:
            raise PasswordException('La contraseña introducida es incorrecta')