from rest_framework import serializers
from .models import OrganizacionModel
from rest_framework.reverse import reverse


class OrganizacionSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='organizacion-detail',lookup_field='pk')
    class Meta:
        model = OrganizacionModel
        fields = [
            'url',
            'edit_url',
            'id',
            'ruc',
            'razon_social',
            'nombre_comercial',
            'tipo',
            'ciiu',
            'direccion_legal',
            'full_direction',
            'pais_organizacion',
            'departamento_organizacion',
            'provincia_organizacion',
            'distrito_organizacion',
            'is_enabled',
            'created_at',
            'members',
            'user'
        ]

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('organizacion-update',kwargs={"pk":obj.id},request=request)