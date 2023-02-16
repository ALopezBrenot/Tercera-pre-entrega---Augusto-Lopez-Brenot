from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render (request, 'AppEntrega/inicio.html')

def pacientes(request):

    if request.method == 'POST':
        nuevo_paciente = Paciente(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            mail = request.POST['mail'],
            DNI = request.POST['DNI'],
            fecha_nac = request.POST['fecha_nac'],
            sexo = request.POST['sexo']
        )
        nuevo_paciente.save()

        return redirect('inicio')

    return render (request, 'AppEntrega/pacientes.html')

def profesionales(request):

    if request.method == 'POST':
        mi_formulario = ProfesionalesFormulario(request.POST)

        # validamos la info recibida del formulario
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_profesional = Profesional(
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                mail = informacion['mail'],
                matricula = informacion['matricula'],
                profesion = informacion['profesion']
            )
            nuevo_profesional.save()

            return redirect('inicio')
    else:
        mi_formulario = ProfesionalesFormulario()
    return render (request, 'AppEntrega/profesionales.html', {'formulario_profesionales': mi_formulario})

def test_covid(request):

    if request.method == 'POST':
        mi_formulario = TesteosFormulario(request.POST)

        # validamos la info recibida del formulario
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_testeo = TestCovid(
                DNI_pac = informacion['DNI_pac'],
                estado = informacion['estado'],
                resultado = informacion['resultado'],
                profesional = informacion['profesional'],
                fecha = informacion['fecha']
            )
            nuevo_testeo.save()

            return redirect('inicio')
    else:
        mi_formulario = TesteosFormulario()
    return render (request, 'AppEntrega/test_covid.html', {'formulario_testeos': mi_formulario})

def resultado_test(request):
    return render(request, 'AppEntrega/resultado_test.html')

def buscar(request):
    if request.GET['DNI_pac']:
        paciente = request.GET['DNI_pac']
        resultado = TestCovid.objects.filter(DNI_pac__icontains = paciente)
        return render(request, 'AppEntrega/resultado-busqueda.html', {'paciente': paciente, 'resultado': resultado})

    else:
        respuesta = 'No se encontró ese paciente.'

    return HttpResponse(respuesta)
