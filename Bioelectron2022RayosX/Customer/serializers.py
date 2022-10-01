from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import OrganizacionModel,DepartamentoModel,AreasModel,ContactosModel,User_Organizaciones_Model,User_Departamentos_Model,User_Areas_Model
from rest_framework.reverse import reverse

class AreasSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='area-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = AreasModel
        fields = ['url','edit_url','delete_url','id','nombre_area','ubicacion','is_enabled','created_at','actions']
        depth=1 

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

class DepartamentoSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='departamento-detail',lookup_field='pk')
    class Meta:
        model = DepartamentoModel
        fields = ['url','edit_url','delete_url','id','nombre_departamento','direccion_departamento','pais_departamento','departamento_departamento','provincia_departamento','distrito_departamento','is_enabled','created_at','members','contactos','actions']
        depth=1 

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
      
class OrganizacionSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)    
    delete_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='organizacion-detail',lookup_field='pk')
    class Meta:
        model = OrganizacionModel
        fields = ('url','edit_url','delete_url','id','ruc','razon_social','nombre_comercial','tipo','ciiu','direccion_legal','full_direction','pais_organizacion','departamento_organizacion','provincia_organizacion','distrito_organizacion','is_enabled','created_at','members','actions',)
        depth=1 

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