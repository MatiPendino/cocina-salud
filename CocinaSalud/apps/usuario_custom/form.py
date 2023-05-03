from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput({
                'placeholder': 'Nombre...',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput({
                'placeholder': 'Apellido...',
                'class': 'form-control'
            }),
            'email': forms.EmailInput({
                'placeholder': 'Correo electrónico...',
                'class': 'form-control'
            }),
            'username': forms.TextInput({
                'placeholder': 'Nombre de usuario...',
                'class': 'form-control'
            })
        }
