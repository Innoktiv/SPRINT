from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido', 'edad', 'email','fecha_contratacion')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password: forms.CharField(label="Contrasena", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmacion Contrasena", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password', 'password2']
        help_texts = {k: "" for k in fields}

        
    #Refactorizado
    # nombre=forms.CharField(max_length=50, required=True, label="Nombre Profesor")
    # apellido=forms.CharField(max_length=50, required=True, label="Apellido Profesor")
    # edad=forms.IntegerField(required=True)
    # email=forms.EmailField(required=True)
    # fecha_contratacion=forms.DateField(required=True)

