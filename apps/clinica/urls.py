from django.urls import path
from .views import crearPaciente, crearConsulta, listarPaciente, editarPaciente

urlpatterns=[
    path('crear_paciente/', crearPaciente ,name= 'crear_paciente'),
    path('crear_consulta/', crearConsulta ,name= 'crear_consulta'),
    path('listar_paciente/',listarPaciente, name = 'listar_paciente'),
    path('editar_paciente/<int:expediente>',editarPaciente, name = 'editar_paciente'),
    
]
