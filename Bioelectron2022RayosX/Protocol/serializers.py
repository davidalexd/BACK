from pyexpat import model
from .models import ProtocolsModel,SeccionesModel, User_Protocolos_Model, User_Pruebas_Calculo_Model, User_Pruebas_Model, User_Pruebas_Opciones_Model, User_Secciones_Model, User_Variables_Model,VariablesModel,PruebasModel,PruebaCalculoModel,PruebaOpcionesModel
from rest_framework import serializers
from rest_framework.reverse import reverse
from Operations.serializers import OperacionesSerializer
from Operations.models import OperacionesModel

class VariablesSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='variable-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = VariablesModel
        fields = ("id","nombre_variable","range_variable","valor_defecto","is_enabled","created_at","url","edit_url","delete_url","actions")

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

    def get_actions(self,obj):
        Uc = []
        autores = User_Variables_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "calculo":x.model.nombre_variable,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

class PruebaCalculoSerializer(serializers.ModelSerializer):
    operacion = OperacionesSerializer(many=True,read_only=True)
    operacion_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=OperacionesModel.objects.all())
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='prueba-calculo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = PruebaCalculoModel
        fields = ("id","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","created_at","url","edit_url","delete_url","operacion","actions","operacion_ids")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-calculo-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-calculo-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_Pruebas_Calculo_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "calculo":x.model.id,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

    def update(self, instance, validated_data):
        if 'operacion' in validated_data:
            instance.operacion.set(validated_data['operacion'])
        instance.save()
        return instance

class PruebaOpcionesSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='prueba-opcion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = PruebaOpcionesModel
        fields = ("id","pruebas_opciones","is_enabled","created_at","url","edit_url","delete_url","actions")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-opcion-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-opcion-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_Pruebas_Opciones_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "Opciones":x.model.pruebas_opciones,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc
        

class PruebasSerializer(serializers.ModelSerializer):
    calculo = PruebaCalculoSerializer(many=True,read_only=True)
    calculo_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=PruebaCalculoModel.objects.all())
    opcion = PruebaOpcionesSerializer(many=True,read_only=True)
    opcion_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=PruebaOpcionesModel.objects.all())
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='prueba-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = PruebasModel
        fields = ("id","pruebas_titulo","pruebas_contexto","is_enabled","created_at","url","edit_url","delete_url","calculo","opcion","actions","calculo_ids","opcion_ids")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prueba-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_Pruebas_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "prueba":x.model.pruebas_titulo,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

    def update(self, instance, validated_data):
        if 'calculo' in validated_data:
            instance.calculo.set(validated_data['calculo'])
        if 'opcion' in validated_data:
            instance.opcion.set(validated_data['opcion'])
        instance.save()
        return instance

class SeccionesSerializer(serializers.ModelSerializer):
    pruebas = PruebasSerializer(many=True,read_only=True)
    pruebas_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=PruebasModel.objects.all())
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='seccion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = SeccionesModel
        fields = ("id","secciones_titulo","secciones_contexto","is_enabled","created_at","url","edit_url","delete_url","pruebas","actions","pruebas_ids")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('seccion-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('seccion-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_Secciones_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.secciones_titulo,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

    def update(self, instance, validated_data):
        if 'pruebas' in validated_data:
            instance.pruebas.set(validated_data['pruebas'])
        instance.save()
        return instance

class ProtocolosSerializer(serializers.ModelSerializer):
    secciones = SeccionesSerializer(many=True,read_only=True)
    secciones_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=SeccionesModel.objects.all())
    variables = VariablesSerializer(many=True,read_only=True)
    variables_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=VariablesModel.objects.all())
    actions = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='protocolo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = ProtocolsModel
        fields = ("id","protocolo_titulo","protocolo_detalles","is_enabled","created_at","url","edit_url","delete_url","secciones","variables","actions","secciones_ids","variables_ids")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('protocolo-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('protocolo-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_Protocolos_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.protocolo_titulo,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

    def update(self, instance, validated_data):
        if 'secciones' in validated_data:
            instance.secciones.set(validated_data['secciones'])
        if 'variables' in validated_data:
            instance.variables.set(validated_data['variables'])
        instance.save()
        return instance


class UserProtocolosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Protocolos_Model
        fields = '__all__'

class UserSeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Secciones_Model
        fields = '__all__'

class UserPruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Pruebas_Model
        fields = '__all__'

class UserPruebasCalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Pruebas_Calculo_Model
        fields = '__all__'

class UserPruebasOpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Pruebas_Opciones_Model
        fields = '__all__'

class UserVariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Variables_Model
        fields = '__all__'