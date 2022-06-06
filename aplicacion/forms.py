from django import forms

from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido', 'edad', 'email','fecha_contratacion')

        
    #Refactorizado
    # nombre=forms.CharField(max_length=50, required=True, label="Nombre Profesor")
    # apellido=forms.CharField(max_length=50, required=True, label="Apellido Profesor")
    # edad=forms.IntegerField(required=True)
    # email=forms.EmailField(required=True)
    # fecha_contratacion=forms.DateField(required=True)

