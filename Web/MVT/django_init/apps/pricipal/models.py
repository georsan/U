from django.db import models

# Create your models here.
 
 #tipodocumento
class tipodocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre
 #documentos
class ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
 #Tabla persona
class persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    idtipodocumento = models.ForeignKey(tipodocumento, on_delete=models.CASCADE)
    documento = models.IntegerField(max_length=12  )
    lugarresidencia = models.ForeignKey(ciudad,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField(max_length=10)
    usuario = models.CharField(max_length=12)
    password = models.CharField(max_length=10)      