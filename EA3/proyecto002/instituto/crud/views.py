from django.shortcuts import render
from .models import Marca

# Create your views here.
def marca(request):
    #orm
    marcas = Marca.objects.all() # select * from marca
    context = {"marcas": marcas}
    return render(request, 'marca.html', context)