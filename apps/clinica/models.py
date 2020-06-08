from django.db import models

# Create your models here.


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    expediente = models.IntegerField('No.Expediente',blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    dui = models.CharField('DUI', max_length=10, blank=False,null=False)
    sexo = models.CharField('Sexo', max_length=1, blank=False, null=False)
    email = models.CharField('email',max_length=100,blank=False, null=False)
    estadoCivil = models.CharField('estadoCivil', max_length=10, blank=False,null=False)
    telefono = models.CharField('Telefono', max_length=9, blank=False,null=False)
    fechaNaci = models.DateField('Fecha de Nacimiento',blank=False,null=False)
    direccion = models.TextField('Direccion',max_length=300, blank=False,null=False)
    departamento = models.CharField('Departamento',max_length=100,blank=False,null=False)
    municipio = models.CharField('Municipio',max_length=100,blank=False,null=False)
    altura = models.FloatField('Altura',blank=False,null=False)
    peso = models.FloatField('Peso', blank=False,null=False)
    
    class Meta:
            verbose_name = 'Paciente'
            verbose_name_plural = 'Pacientes'
            ordering = ['id_paciente']

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Medico(models.Model):
    idMedico= models.AutoField('IdMedico',primary_key=True)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    dui = models.CharField('DUI', max_length=10, blank=False,null=False)
    sexo = models.CharField('Sexo', max_length=1, blank=False, null=False)
    email = models.CharField('email',max_length=100,blank=False, null=False)
    estadoCivil = models.CharField('estadoCivil', max_length=6, blank=False,null=False)
    telefono = models.IntegerField('Telefono', blank=False,null=False)
    fechaNaci = models.DateField('Fecha de Nacimiento',blank=False,null=False)
    direccion = models.TextField('Direccion',max_length=300, blank=False,null=False)
    departamento = models.CharField('Departamento',max_length=100,blank=False,null=False)
    municipio = models.CharField('Municipio',max_length=100,blank=False,null=False)
    altura = models.IntegerField('Altura',blank=False,null=False)
    peso = models.IntegerField('Peso', blank=False,null=False)

    class Meta:
        verbose_name='Medico'
        verbose_name_plural= 'Medicos'
        ordering=['idMedico']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Consulta (models.Model):
    idConsulta = models.AutoField(primary_key=True)
    idMedico = models.CharField('IdMedico', max_length=4, blank=False, null=False)
    idPaciente = models.CharField('IdPaciente', max_length=4, blank=False, null=False)
    idEspecialidad = models.CharField('IdEspecialidad', max_length=4, blank=False, null=False)
    idCita = models.CharField('IdCita',max_length=4,blank=False, null=False)
    fecha= models.DateField('FechaConsulta', blank=False, null=False)

    class Meta:
            verbose_name='Consulta'
            verbose_name_plural= 'Consultas'
            ordering=['idConsulta']
    
    def __str__(self):
        return self.idPaciente


class Referencia (models.Model):
    idReferencia = models.AutoField(primary_key =True)
    idMedico = models.CharField('IdMedico',max_length=4,blank=False,null=False)
    nombre= models.CharField('Nombre', max_length=50, blank=False, null=False)
    cargo = models.CharField('Cargo', max_length=50, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=50, blank=False, null=False)
    lugarReferencia = models.CharField('LugarReferencia', max_length=50,blank=False,null=False)
    tipoReferencia = models.CharField('TipoReferencia', max_length=50, blank=False, null=False)

    class Meta:
            verbose_name='Referencia'
            verbose_name_plural= 'Referencias'
            ordering=['idReferencia']
    
    def __str__(self):
        return self.nombre + ' ' + self.lugarReferencia
