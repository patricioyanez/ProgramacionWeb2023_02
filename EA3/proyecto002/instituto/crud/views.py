from django.shortcuts import render
from .models import Marca

# Create your views here.
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