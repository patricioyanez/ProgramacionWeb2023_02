from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre
    
# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud

class Categoria(models.Model):
    idCategoria= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre
    

