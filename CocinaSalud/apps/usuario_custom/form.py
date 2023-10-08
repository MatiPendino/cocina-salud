from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}
        ),
        required=True
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre...', 'class': 'form-control'}
        ),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Apellido...', 'class': 'form-control'}
        ),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Correo electrónico...', 'class': 'form-control'}
        ),
        required=True
    )
