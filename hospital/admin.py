from django.contrib import admin
from hospital.models import *

#admin.site.register(DepartamentoMedico)

@admin.register(DepartamentoMedico)
class DepartamentoMedico(admin.ModelAdmin):
    # columnas visibles en la lista del modelo
    list_display = ("nombre", "nro_departamento", "email_dpto", "fecha_de_creacion")
    # columnas con enlaces clickeables para entrar en el detalle
    list_display_links = ("nombre",)	#con coma al final xq es una tupla
    # campos por los que se pueden buscar
    search_fields = ("nro_departamento",)
    # filtros laterales
    list_filter = ("fecha_de_creacion",)
    # orden por defecto
    ordering = ("nro_departamento", "nombre")
    # campos de solo lectura
    readonly_fields = ("fecha_de_creacion",)
