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
    form_guardado = False

    if request.method == 'POST':
        form = FormSocios(request.POST)
        if form.is_valid():
            form.save()
            form_guardado = True
            form = FormSocios()
    data = {'form': form, 'form_guardado': form_guardado}
    return render(request, 'agregar.html', data)
