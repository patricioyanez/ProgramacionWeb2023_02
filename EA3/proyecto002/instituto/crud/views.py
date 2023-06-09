from django.shortcuts import render
from .models import Marca, Categoria,Genero

# importar los Form
from .forms import ClienteForm
# Create your views here.

# importar decoradores
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, 'menu.html')


# crear modelo producto y usar la clase Forms de Django para crear formulario
@login_required
def clienteForm(request):
    context = {'form':  ClienteForm()}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()
                context['exito']='Datos guardados'
            else:                
                context['error']='Datos No guardados'

    return render(request, 'clienteForm.html', context)

@login_required
def categoria(request):
    #orm
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Categoria.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Categoria.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Categoria.objects.all() # select * from categoria
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'categoria.html', context)
@login_required
def genero(request):
    #orm
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Genero.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Genero.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Genero.objects.all() # select * from genero
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Genero.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Genero.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'genero.html', context)
@login_required
def marca(request):
    #orm
    context = {}
    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        if 'Grabar' in request.POST: # fue presionado el grabar
            if id == 0: # insert
                Marca.objects.create(nombre=nombre, activo=activo)
                context = {'exito' : 'Los datos fueron guardados'}
            else: # update
                try:
                    item = Marca.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito' : 'Los datos fueron guardados'}
                except:                    
                    context = {'error' : 'Los datos NO fueron guardados'}
        elif 'Listar' in request.POST:
            listado = Marca.objects.all() # select * from marca
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                context = {'item': item }
            except:
                context = {'error' : 'El id no fue encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                item.delete()
                context = {'exito' : 'El id fue ELIMINADO'}
            except:
                context = {'error' : 'El id no fue encontrado'}

    return render(request, 'marca.html', context)