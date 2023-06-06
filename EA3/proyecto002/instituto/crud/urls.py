from . import views
from django.urls import path

urlpatterns =[
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('genero', views.genero, name='genero'),
    path('clienteForm', views.clienteForm, name='clienteForm'),
]
# EJERCICIO: crear crud para categoria y genero
# para acceder al formulario marca
# http://127.0.0.1:8000/crud/marca