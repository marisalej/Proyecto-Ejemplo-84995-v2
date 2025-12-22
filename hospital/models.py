from django.db import models

class DepartamentoMedico(models.Model):
    nombre = models.CharField(max_length=50)
    nro_departamento = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    email_dpto = models.EmailField() #validacion simple

    def __str__(self):
        return f"Nombre: {self.nombre} / Nro_dpto: {self.nro_departamento}"
    