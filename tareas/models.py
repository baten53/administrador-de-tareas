from django.db import models

class Usuario(models.Model):
    pnombre = models.CharField(max_length=20)
    snombre = models.CharField(max_length=20)


class Estado(models.Model):
    nombre = models.CharField(max_length=15)    


class Tarea(models.Model):
    nombre = models.CharField(max_length=25)
    responsable = models.ForeignKey('Usuario', 
        on_delete=models.CASCADE,)
    descripcion = models.CharField(max_length=60)
    status = models.ForeignKey('Estado',
        on_delete=models.CASCADE,)

