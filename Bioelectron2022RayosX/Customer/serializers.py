from rest_framework import serializers
from .models import Dpt_org_Model, OrganizacionModel,DepartamentoModel,AreasModel,ContactosModel
from rest_framework.reverse import reverse

class ContactosSerialezer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='contacto-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = ContactosModel
        fields = (
            'id',
            'nombre',
            'apellidos',
            'dni',
            'numero_telefono',
            'correo',
            'cargo',
            'is_enabled',
            'created_at',
            'updated_at',
            'url',
            'edit_url',
            'delete_url')
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('contacto-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('contacto-delete',kwargs={"pk":obj.id},request=request)

class AreasSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='area-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = AreasModel
        fields = (
            'id',
            'nombre_area',
            'ubicacion',
            'is_enabled',
            'created_at',
            'updated_at',
            'url',
            'edit_url',
            'delete_url')
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('area-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('area-delete',kwargs={"pk":obj.id},request=request)

    
    def update(self, instance, validated_data):
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        if 'contactos' in validated_data:
            instance.contactos.set(validated_data['contactos'])
        instance.save()
        return instance

class DepartamentoSerializer(serializers.ModelSerializer): 
    members = AreasSerializer(many=True,read_only=True)
    contactos = ContactosSerialezer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=AreasModel.objects.filter(is_enabled=True))
    contactos_ids = serializers.PrimaryKeyRelatedField(
        source='contactos',
        write_only=True,
        many=True,
        queryset=ContactosModel.objects.filter(is_enabled=True))
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='departamento-detail',lookup_field='pk')

    class Meta:
        model = DepartamentoModel
        fields = (  
            'id',
            'nombre_departamento',
            'direccion_departamento',
            'pais_departamento',
            'departamento_departamento',
            'provincia_departamento',
            'distrito_departamento',
            'is_enabled',
            'created_at',
            'updated_at',
            'url',
            'edit_url',
            'delete_url',
            'members',
            'contactos',
            'members_ids',
            'contactos_ids'
            )

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('departamento-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('departamento-delete',kwargs={"pk":obj.id},request=request)

    def update(self, instance, validated_data):
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        if 'contactos' in validated_data:
            instance.contactos.set(validated_data['contactos'])
        instance.save()
        return instance


class OrganizacionSerializer(serializers.ModelSerializer): 
    members = DepartamentoSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=DepartamentoModel.objects.filter(is_enabled=True))
    edit_url = serializers.SerializerMethodField(read_only = True)    
    delete_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='organizacion-detail',lookup_field='pk')
    
    class Meta:
        model = OrganizacionModel
        fields = (
            'id',
            'ruc',
            'razon_social',
            'nombre_comercial',
            'tipo',
            'ciiu',
            'direccion_legal',
            'pais_organizacion',
            "full_direction",
            'departamento_organizacion',
            'provincia_organizacion',
            'distrito_organizacion',
            'is_enabled',
            'created_at',
            'updated_at',
            'url',
            'edit_url',
            'delete_url',
            'members',
            'members_ids'
            )

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('organizacion-update',kwargs={"pk":obj.id},request=request)
        
    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('organizacion-delete',kwargs={"pk":obj.id},request=request)

    def update(self, instance, validated_data):
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        instance.save()
        return instance
