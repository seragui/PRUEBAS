from django.contrib import admin
from .models import Paciente,Medico,Consulta,Referencia

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Referencia)