from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    DNI = models.IntegerField()
    fecha_nac = models.DateField()
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return (self.DNI)

class Profesional(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    matricula = models.IntegerField()
    profesion = models.CharField(max_length=20)

    def __str__(self):
        return (self.nombre + ' '+ self.apellido)

class TestCovid(models.Model):
    DNI_pac = models.IntegerField()
    estado = models.BooleanField()
    resultado = models.CharField(max_length=20)
    profesional = models.CharField(max_length=50)
    fecha = models.DateField()
