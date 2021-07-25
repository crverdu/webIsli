
from django.db import models

class Dispositivo(models.Model):
    description=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.description}"
class Curso(models.Model):
    grado=models.CharField(max_length=3)

    def __str__(self):
        return f"{self.grado} "


class Encuesta (models.Model):
    apellido=models.CharField(max_length=80)
    nombre=models.CharField(max_length=80)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE,related_name='curs')
    burbuja=models.CharField(max_length=1)
    email=models.EmailField()
    dispositivo=models.ManyToManyField(Dispositivo,related_name="dispAlum")
    bio=models.CharField(max_length=200)
    herramientas=models.CharField(max_length=200)

    def __str__(self):
        return f"ID Encuesta # {self.id}: {self.apellido} {self.nombre} {self.curso} {self.burbuja} {self.email} {self.dispositivo} {self.bio} {self.herramientas} "
