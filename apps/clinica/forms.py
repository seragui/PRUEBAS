from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['expediente','nombre','apellidos','dui','sexo','email','estadoCivil','telefono','fechaNaci', 'direccion', 'departamento','municipio','altura','peso']