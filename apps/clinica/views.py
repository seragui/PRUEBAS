from django.shortcuts import render, redirect
from .models import Paciente, Consulta
from .forms import PacienteForm, ConsultaForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def Home (request):
    return render(request,'index.html')


def crearPaciente(request):
    if request.method == 'POST':
        print(request.POST)
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            paciente_form.save()
            return redirect('index.html')
    else :
        paciente_form = PacienteForm()
    return render(request,'clinica/crear_paciente.html',{'paciente_form':paciente_form})


def crearConsulta(request):
    if request.method == 'POST':
        print(request.POST)
        consulta_form = ConsultaForm(request.POST)
        if consulta_form.is_valid():
            consulta_form.save()
            return redirect('index')
    else :
        consulta_form = ConsultaForm()
    return render(request,'clinica/crear_consulta.html',{'consulta_form':consulta_form})


def listarPaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/listar_paciente.html',{'pacientes':pacientes})

def editarPaciente(request,expediente):
    error = None
    try:
        paciente = Paciente.objects.get(expediente = expediente)
        if request.method == 'GET' :
            paciente_form = PacienteForm(instance = paciente)
        else:
            paciente_form = PacienteForm(request.POST, instance = paciente)
            if paciente_form.is_valid():
                paciente_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e :
        error = e

    return render(request,'clinica/crear_paciente.html',{'paciente_form':paciente_form,'error':error})


