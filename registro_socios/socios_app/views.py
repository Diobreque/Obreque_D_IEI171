from operator import index
from django import forms
from django.shortcuts import render, redirect
from socios_app.models import Socio
from socios_app.forms import FormSocios
# Create your views here.


def index(request):
    data = {
    "title": "Usuario",
    "titulo": "Usuario",
    "nombre": "Diego Obreque Molina",
    "email": "diego.obreque05@inacapmail.cl",
    "carrera": "Analista Programador",
    "sede": "Temuco",
    "foto1": "user.jpeg"
    }

    return render(request, 'index.html', data)

def listadoSocios(request):
    socios = Socio.objects.all()
    data = {'socios' : socios}
    return render(request, 'socios_lista.html', data)


def agregarSocios(request):
    data = {"title": "Agregar", "accion": "Agregar Socio"}
    
    if request.method == 'POST':
        form = FormSocios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/agregar')
        else:
            data['form'] = form
            return render(request, 'agregar.html', data)
    else:
        form = FormSocios()
    
    data['form'] = form
    return render(request, 'agregar.html', data)


def editarSocios(request, soc_id):
    socio = Socio.objects.get(id_socio = soc_id)
    form = FormSocios(instance=socio)
    data = {'form': form, "title" : "Editar", "accion" : "Editar Socio"}

    if (request.method == "POST"):
        form = FormSocios(request.POST, instance=socio)
        if (form.is_valid()):
            form.save()
            return redirect('/socios')
        else:
            data['form'] = form
            return render(request, 'agregar.html', data)
    return render (request, 'agregar.html', data)


def eliminarSocios(request, soc_id):
    socio = Socio.objects.get(id_socio = soc_id)
    socio.delete()
    return redirect('/socios')