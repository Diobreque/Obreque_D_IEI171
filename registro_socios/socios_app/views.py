from operator import index
from django.shortcuts import render
from .models import Socio
from .forms import FormSocios
# Create your views here.

def listadoSocios(request):
    socios = Socio.objects.all()
    data = {'socios' : socios}
    return render(request, 'socios_lista.html', data)

def agregarSocios(request):
    form = FormSocios()

    if (request.method == 'POST'):
        form = FormSocios(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
  
    data = {'form': form}
    return render (request, 'agregar.html', data)