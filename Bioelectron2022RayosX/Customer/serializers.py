from rest_framework import serializers
from .models import OrganizacionModel



class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizacionModel
        fields = [
            'ruc',
            'razon_social',
            'nombre_comercial',
            'tipo',
            'ciiu',
            'full_direction',
            'pais_organizacion',
            'departamento_organizacion',
            'provincia_organizacion',
            'distrito_organizacion',
            'members'
        ]