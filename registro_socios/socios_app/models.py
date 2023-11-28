from django.db import models

# Create your models here.
# • Para el sistema se necesitará almacenar, el nombre del socio, fecha incorporación, año de
# nacimiento, teléfono, correo electrónico, sexo, estado (Vigente, Suspendido, Retirado),
# observacion
# • Se debe implementar el CRUD completo utilizando funciones.
# • Todos los campos son obligatorios, excepto la observación, la cantidad de personas debe
# estar entre 1 y 15.
# Todos los campos son obligatorios, excepto la observación, la cantidad de personas debe
# estar entre 1 y 15, validación de correo electrónico, el nombre del socio no puede superar
# los 80 caracteres.

selector_sexo = [(1,'Femenino'),(2,'Masculino')(3,'Otro')]

class Socios(models.Model):
    id_socio = models.AutoField(primary_key=True)
    nombre_socio = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    anio_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo_electronico = models.DateField()
    sexo = models.IntegerField(
        null=False, blank=False,
        choices=selector_sexo
    )
    def __str__(self):
        return self.nombre_socio