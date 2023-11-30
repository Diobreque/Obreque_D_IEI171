from django.db import models

# Create your models here.

selector_sexo = [(1,'Femenino'),(2,'Masculino'),(3,'Otro')]
selector_estado = [(1,'Vigente'),(2,'Suspendido'),(3,'Retirado')]

class Socio(models.Model):
    id_socio = models.AutoField(primary_key=True)
    nombre_socio = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    anio_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo_electronico = models.EmailField()
    sexo = models.IntegerField(
        null=False, blank=False,
        choices=selector_sexo
    )
    estado = models.IntegerField(
        null=False, blank=False,
        choices=selector_estado
    )
    def __str__(self):
        return self.nombre_socio