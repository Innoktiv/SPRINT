from django.shortcuts import render, redirect  
from django.http import HttpResponse

from .models import Profesor
from .forms import ProfesorForm

# Create your views here.
def index(request):
    
    listado = Profesor.objects.all()   
    return render(request, 'aplicacion/index.html', {'context':listado})

def formulario(request):
    return render(request, 'aplicacion/formulario.html',)


def create(request):
    form = ProfesorForm()
    
    if request.method == 'POST':
        #print(request.POST)
        form = ProfesorForm(request.POST)

        if form.is_valid():
            profesor=Profesor()
            profesor.nombre=form.cleaned_data['nombre']
            profesor.apellido=form.cleaned_data['apellido']
            profesor.edad=form.cleaned_data['edad']
            profesor.email=form.cleaned_data['email']
            profesor.fecha_contratacion=form.cleaned_data['fecha_contratacion']
            profesor.save()
        else:
            print('Invalido')
        return redirect('/aplicacion')

    return render(request, 'aplicacion/create.html', {'form': form})  