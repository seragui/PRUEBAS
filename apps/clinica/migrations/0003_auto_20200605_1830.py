# Generated by Django 3.0.6 on 2020-06-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20200605_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='Telefono'),
        ),
    ]
