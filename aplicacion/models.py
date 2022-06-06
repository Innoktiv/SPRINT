from ssl import VerifyMode
from django.db import models
from django.forms import CharField
import datetime

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField(verbose_name="Mail del Profesor")
    fecha_contratacion=models.DateField(datetime.date.today())

    def __str__(self):
        return self.nombre
    
class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


