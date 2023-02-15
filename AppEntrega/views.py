from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render (request, 'AppEntrega/inicio.html')

def pacientes(request):
    return render (request, 'AppEntrega/pacientes.html')

def profesionales(request):
    return render (request, 'AppEntrega/profesionales.html')

def test_covid(request):
    return render (request, 'AppEntrega/test_covid.html')

