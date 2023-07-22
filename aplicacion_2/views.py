from django.shortcuts import render
from aplicacion_2.models import registroUsuarios, Proveedores
from .forms import registroForm, proveedoresForm



#  USUARIOS

def primeraFuncion(request):
    return render(request, 'landing.html')


def formularioContacto(request):
    data = {
        'form': registroForm()
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "USUARIO REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro.html', data)


def informeUsuarios(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroUsuarios.objects.all()
    #data = {
    #    'usuarios': usuarios
    #}
    return render(request, 'salida.html', {'usuarios': usuarios})




# EMPRESAS PROVEEDORAS

def registroProveedores(request):
    data = {
        'form_prov': proveedoresForm()
    }
    if request.method == 'POST':
        formulario_prov = proveedoresForm(data=request.POST)
        if formulario_prov.is_valid():
            formulario_prov.save()
            data["mensaje"] = "PROVEEDOR REGISTRADO !!!"
        else:
            data["form_prov"] = formulario_prov
    return render(request, 'registro_empresa.html', data)


def informeProveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'salida_empresas.html', {'proveedores': proveedores})