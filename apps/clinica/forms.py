from django import forms
from .models import Paciente,Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['expediente','nombre','apellidos','dui','sexo','email','estadoCivil','telefono','fechaNaci', 'direccion', 'departamento','municipio','altura','peso']


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields= ['idMedico','idPaciente','idEspecialidad','idCita','fecha']
    