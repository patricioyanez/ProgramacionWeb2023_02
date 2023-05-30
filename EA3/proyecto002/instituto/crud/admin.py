from django.contrib import admin
from .models import Marca, Categoria, Genero, Cliente
# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Genero)
admin.site.register(Cliente)