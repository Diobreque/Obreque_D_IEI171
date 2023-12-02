from operator import index
from django import forms
from django.shortcuts import render, redirect
from socios_app.models import Socio
from socios_app.forms import FormSocios
# Create your views here.

def listadoSocios(request):
    socios = Socio.objects.all()
    data = {'socios' : socios}
    return render(request, 'socios_lista.html', data)


def agregarSocios(request):
    if request.method == 'POST':
        form = FormSocios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/agregar')
        else:
            return render(request, 'agregar.html', {'form': form})
    else:
        form = FormSocios()
    return render(request, 'agregar.html', {'form': form})



def eliminarSocios(request, soc_id):
    socio = Socio.objects.get(id_socio = soc_id)
    socio.delete()
    return redirect('/socios')

def editarSocios(request, soc_id):
    socio = Socio.objects.get(id_socio = soc_id)
    form = FormSocios(instance=socio)

    if (request.method == "POST"):
        form = FormSocios(request.POST, instance=socio)
        if (form.is_valid()):
            form.save()
        return redirect('/socios')
    data = {'form': form}
    return render (request, 'agregar.html', data)