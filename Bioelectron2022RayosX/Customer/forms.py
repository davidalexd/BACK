from dataclasses import fields
from django import forms
from .models import OrganizacionModel

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = OrganizacionModel,
        fields = [
            "ruc",
            "razon_social",
            "nombre_comercial",
            "tipo",
            "ciiu",
            "direccion_legal",
            "pais_organizacion",
            "departamento_organizacion",
            "provincia_organizacion",
            "distrito_organizacion"
        ]