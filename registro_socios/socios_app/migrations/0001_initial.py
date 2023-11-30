# Generated by Django 4.2.4 on 2023-11-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id_socio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_socio', models.CharField(max_length=80)),
                ('fecha_incorporacion', models.DateField()),
                ('anio_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('correo_electronico', models.DateField()),
                ('sexo', models.IntegerField(choices=[(1, 'Femenino'), (2, 'Masculino'), (3, 'Otro')])),
                ('estado', models.IntegerField(choices=[(1, 'Vigente'), (2, 'Suspendido'), (3, 'Retirado')])),
            ],
        ),
    ]