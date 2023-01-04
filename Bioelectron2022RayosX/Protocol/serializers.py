from .models import ProtocolsModel,SeccionesModel,PruebaCalculoModel,PruebaOpcionesModel
from rest_framework import serializers
from rest_framework.reverse import reverse
from Operations.serializers import OperacionesSerializer
from Operations.models import OperacionesModel

class PruebaCalculoSerializer(serializers.ModelSerializer):
    operacion = OperacionesSerializer(many=True,read_only=True)
    operacion_ids = serializers.PrimaryKeyRelatedField(
        source='operacion',
        write_only=True,
        many=True,
        queryset=OperacionesModel.objects.filter(is_enabled = True))
    url = serializers.HyperlinkedIdentityField(view_name='prueba-calculo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = PruebaCalculoModel
        fields = ("id","pruebas_titulo","pruebas_contexto","is_enabled","created_at","url","edit_url","delete_url","operacion","operacion_ids")

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

    # def update(self, instance, validated_data):
    #     if 'operacion' in validated_data:
    #         instance.operacion.set(validated_data['operacion'])
    #     instance.save()
    #     return instance

class PruebaOpcionesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='prueba-opcion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = PruebaOpcionesModel
        fields = ("id","pruebas_titulo","pruebas_contexto","pruebas_opciones","is_enabled","created_at","url","edit_url","delete_url")

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

class SeccionesSerializer(serializers.ModelSerializer):
    calculo = PruebaCalculoSerializer(many=True,read_only=True)
    calculo_ids = serializers.PrimaryKeyRelatedField(
        source='calculo',
        write_only=True,
        many=True,
        queryset=PruebaCalculoModel.objects.filter(is_enabled = True))
    opcion = PruebaOpcionesSerializer(many=True,read_only=True)
    opcion_ids = serializers.PrimaryKeyRelatedField(
        source='opcion',
        write_only=True,
        many=True,
        queryset=PruebaOpcionesModel.objects.filter(is_enabled = True))
    url = serializers.HyperlinkedIdentityField(view_name='seccion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = SeccionesModel
        fields = ("id","secciones_titulo","secciones_contexto","is_enabled","created_at","url","edit_url","delete_url","calculo","opcion","calculo_ids","opcion_ids")

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

    # def update(self, instance, validated_data):
    #     if 'calculo' in validated_data:
    #         instance.calculo.set(validated_data['calculo'])
    #     if 'opcion' in validated_data:
    #         instance.opcion.set(validated_data['opcion'])
    #     instance.save()
    #     return instance

class ProtocolosSerializer(serializers.ModelSerializer):
    secciones = SeccionesSerializer(many=True,read_only=True)
    secciones_ids = serializers.PrimaryKeyRelatedField(
        source='secciones',
        write_only=True,
        many=True,
        queryset=SeccionesModel.objects.filter(is_enabled=True))
    url = serializers.HyperlinkedIdentityField(view_name='protocolo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = ProtocolsModel
        fields = ("id","protocolo_titulo","is_enabled","created_at","url","edit_url","delete_url","secciones","secciones_ids")

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

    # def update(self, instance, validated_data):
    #     if 'secciones' in validated_data:
    #         instance.secciones.set(validated_data['secciones'])
    #     instance.save()
    #     return instance
