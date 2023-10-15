from django.contrib.auth.models import User
from apps.usuario_custom.models import Usuario
from apps.base.utils import PasswordException

def create_custom_user(pass1, pass2, username, first_name, last_name, email, birth, p_image):
    username_repeated = User.objects.filter(username=username).exists()

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
                Usuario.objects.create(
                    user=new_user,
                    imagen_perfil=p_image,
                    fecha_nacimiento=birth
                )
            else:
                raise PasswordException('La contraseña debe ser mayor o igual a 8 caracteres.')
        else:
            raise PasswordException('Error: las contraseñas no coinciden.')
    else:
        raise PasswordException('Error: ya existe un usuario con ese username.')
    
