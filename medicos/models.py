from django.db import models
import uuid

def generar_code():
    return uuid.uuid4().hex

class Medico(models.Model):
    ESPECIALIDADES = (
        ("Corazon", "Cardiologo"),
        ("Cerebro", "Neurologo"),
        ("Huesos", "Traumatologo"),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_inicio = models.DateField(auto_now_add=True)
    especialidad = models.CharField(choices=ESPECIALIDADES, max_length=50)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )

    def __str__(self):
        return f"Nombre: {self.nombre} - Especialidad: {self.especialidad}"

