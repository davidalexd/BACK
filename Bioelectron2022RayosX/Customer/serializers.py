from rest_framework import serializers
from .models import OrganizacionModel,DepartamentoModel,AreasModel,ContactosModel, User_Contactos_Model,User_Organizaciones_Model,User_Departamentos_Model,User_Areas_Model
from rest_framework.reverse import reverse

class ContactosSerialezer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='contacto-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = ContactosModel
        fields = ('id','nombre','apellidos','dni','numero_telefono','correo','cargo','is_enabled','created_at','url','edit_url','delete_url','actions')
        

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

    def get_actions(self,obj):
        Uc = []
        autores = User_Contactos_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.full_name,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc


class AreasSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='area-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = AreasModel
        fields = ('id','nombre_area','ubicacion','is_enabled','created_at','url','edit_url','delete_url','actions',)
        

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

    def get_actions(self,obj):
        Uc = []
        autores = User_Areas_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.nombre_area,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc
    
    def update(self, instance, validated_data):
        print(validated_data)
        instance.nombre_area = validated_data.get('nombre_area',instance.nombre_area)
        instance.ubicacion = validated_data.get('ubicacion',instance.ubicacion)
        instance.is_enabled = validated_data.get('is_enabled',instance.is_enabled)
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
        queryset=AreasModel.objects.all())
    contactos_ids = serializers.PrimaryKeyRelatedField(
        source='contactos',
        write_only=True,
        many=True,
        queryset=ContactosModel.objects.all())
    actions = serializers.SerializerMethodField(read_only=True)
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
            'url',
            'edit_url',
            'delete_url',
            'members',
            'contactos',
            'actions',
            'members_ids',
            'contactos_ids')

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

    def get_actions(self,obj):
        Uc = []
        autores = User_Departamentos_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "departamento":x.model.nombre_departamento,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

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
        queryset=DepartamentoModel.objects.all())


    actions = serializers.SerializerMethodField(read_only=True)
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
            'url',
            'edit_url',
            'delete_url',
            'actions',
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

    def get_actions(self,obj):
        Uc = []
        autores = User_Organizaciones_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "organizacion":x.model.razon_social,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

    def update(self, instance, validated_data):
        instance.ruc = validated_data.get('ruc',instance.ruc)
        instance.razon_social = validated_data.get('razon_social',instance.razon_social)
        instance.nombre_comercial = validated_data.get('nombre_comercial',instance.nombre_comercial)
        instance.tipo = validated_data.get('tipo',instance.tipo)
        instance.ciiu = validated_data.get('ciiu',instance.ciiu)
        instance.direccion_legal = validated_data.get('direccion_legal',instance.direccion_legal)
        instance.pais_organizacion = validated_data.get('pais_organizacion',instance.pais_organizacion)
        instance.departamento_organizacion = validated_data.get('departamento_organizacion',instance.departamento_organizacion)
        instance.provincia_organizacion = validated_data.get('provincia_organizacion',instance.provincia_organizacion)
        instance.distrito_organizacion = validated_data.get('distrito_organizacion',instance.distrito_organizacion)
        instance.is_enabled = validated_data.get('is_enabled',instance.is_enabled)
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        instance.save()
        return instance




class UserAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Areas_Model
        fields = '__all__'

class UserDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Departamentos_Model
        fields = '__all__'

class UserOrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Organizaciones_Model
        fields = '__all__'

class UserContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Contactos_Model
        fields = '__all__'
        