# Generated by Django 3.0.6 on 2020-05-20 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('idConsulta', models.AutoField(primary_key=True, serialize=False)),
                ('idMedico', models.CharField(max_length=4, verbose_name='IdMedico')),
                ('idPaciente', models.CharField(max_length=4, verbose_name='IdPaciente')),
                ('idEspecialidad', models.CharField(max_length=4, verbose_name='IdEspecialidad')),
                ('idCita', models.CharField(max_length=4, verbose_name='IdCita')),
                ('fecha', models.DateField(verbose_name='FechaConsulta')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['idConsulta'],
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False, verbose_name='IdMedico')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dui', models.CharField(max_length=10, verbose_name='DUI')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('estadoCivil', models.CharField(max_length=6, verbose_name='estadoCivil')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('fechaNaci', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.TextField(max_length=300, verbose_name='Direccion')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('altura', models.IntegerField(verbose_name='Altura')),
                ('peso', models.IntegerField(verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
                'ordering': ['idMedico'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('expediente', models.IntegerField(verbose_name='No.Expediente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dui', models.CharField(max_length=10, verbose_name='DUI')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('estadoCivil', models.CharField(max_length=6, verbose_name='estadoCivil')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('fechaNaci', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.TextField(max_length=300, verbose_name='Direccion')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('altura', models.IntegerField(verbose_name='Altura')),
                ('peso', models.IntegerField(verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['id_paciente'],
            },
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('idReferencia', models.AutoField(primary_key=True, serialize=False)),
                ('idMedico', models.CharField(max_length=4, verbose_name='IdMedico')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('lugarReferencia', models.CharField(max_length=50, verbose_name='LugarReferencia')),
                ('tipoReferencia', models.CharField(max_length=50, verbose_name='TipoReferencia')),
            ],
            options={
                'verbose_name': 'Referencia',
                'verbose_name_plural': 'Referencias',
                'ordering': ['idReferencia'],
            },
        ),
    ]
