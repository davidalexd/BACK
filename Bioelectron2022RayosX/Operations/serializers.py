from asyncio.windows_events import NULL
from .models import CategoryOperacionesModel, OperacionesModel, Opr_Operacion_Variables, VariablesModel
from rest_framework import serializers
from rest_framework.reverse import reverse


class VariablesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='variable-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = VariablesModel
        fields = ("id","nombre_variable","range_variable","valor_defecto","is_enabled","created_at","url","edit_url","delete_url")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('variable-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('variable-delete',kwargs={"pk":obj.id},request=request)


class OperacionesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='operacion-detail',lookup_field='pk')
    operation_url = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    variables = serializers.SerializerMethodField(read_only = True)
    variables_ids = serializers.PrimaryKeyRelatedField(
        source='secciones',
        write_only=True,
        many=True,
        queryset=VariablesModel.objects.filter(is_enabled=True))

    class Meta:
        model = OperacionesModel
        fields = ('id','operacion_titulo','operacion_funcion',"operacion_variable",'operacion_symbol','operacion_contexto','is_enabled','created_at','url','operation_url','edit_url','delete_url','variables','variables_ids')
        

    def get_variables(self,obj):
        request = Opr_Operacion_Variables.objects.filter(operacion = obj.id)
        Uc = []
        for x in request:
            Uc.append(
                {
                    "identificador":x.id,
                    "id":x.variables.id,
                    "nombre_variable": x.variables.nombre_variable,
                    "range_variable": x.variables.range_variable,
                    "valor_defecto": x.variables.valor_defecto,
                    "is_enabled": x.variables.is_enabled,
                    "created_at": x.variables.created_at,
                }
            )
        return Uc


    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('operacion-update',kwargs={"pk":obj.id},request=request)

    def get_operation_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse(obj.operacion_funcion,kwargs={"global":'['},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('operacion-delete',kwargs={"pk":obj.id},request=request)


class CategoriaOperacionesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='categoria-operacion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    operaciones = OperacionesSerializer(many=True,read_only=True)
    operaciones_ids = serializers.PrimaryKeyRelatedField(
        source='operaciones',
        write_only=True,
        many=True,
        queryset=OperacionesModel.objects.filter(is_enabled=True))

    class Meta:
        model = CategoryOperacionesModel
        fields = ('id','category_operacion_titulo','category_operacion_contexto','is_enabled','created_at','url','edit_url','delete_url','operaciones','operaciones_ids')
        
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('categoria-operacion-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('categoria-operacion-delete',kwargs={"pk":obj.id},request=request)

