from django.db import models

# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud

# Create your models here.
class Marca(models.Model):
    idMarca= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    idCategoria= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre
    

class Genero(models.Model):
    idGenero= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    idCliente= models.AutoField(primary_key=True)
    rut = models.IntegerField(unique=True, null=False, blank=False)
    dv = models.CharField(max_length=1,null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, unique=False)
    apellido = models.CharField(max_length=50, null=False, unique=False)
    telefono = models.CharField(max_length=50, null=False, unique=False)
    email = models.EmailField(max_length=50, null=False, unique=False)
    genero = models.ForeignKey(Genero, db_column='idGenero',
                               on_delete=models.CASCADE,
                               null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
