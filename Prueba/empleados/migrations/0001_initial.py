# Generated by Django 4.1.1 on 2022-09-29 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('presupuesto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nif', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('codigo_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.departamento')),
            ],
        ),
    ]
