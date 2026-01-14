from django import forms
from hospital.models import DepartamentoMedico


class DepartamentoMedicoForm(forms.ModelForm):
    class Meta:
        model = DepartamentoMedico
        fields = [
            "nombre",
            "nro_departamento",
            "email_dpto",
            "nro_empleados",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_departamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_empleados': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_dpto': forms.EmailInput(attrs={'class': 'form-control'}),
#            'fecha_de_creacion': forms.DateInput(attrs={'class': 'form-control'})
        }
        
class DepartamentoMedicoUpdateForm(forms.ModelForm):
    class Meta:
        model = DepartamentoMedico
        fields = [
            "nro_departamento",
            "email_dpto",
            "nro_empleados",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_departamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_empleados': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_dpto': forms.EmailInput(attrs={'class': 'form-control'}),
#            'fecha_de_creacion': forms.DateInput(attrs={'class': 'form-control'})
        }
        