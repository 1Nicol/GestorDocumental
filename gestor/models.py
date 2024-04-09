from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    sub_departamento = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    folio = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
