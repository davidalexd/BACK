from CompanyMachine.models import MedidoresModel
from Machine.models import SistemaModel, TuboModel
from Customer.models import AreasModel,DepartamentoModel,OrganizacionModel
from .models import ReportsCategoryModel, ReportsFormatsModel,PruebaCalculoModel,PruebaOpcionesModel, ReportsReporteModel,SeccionesModel
from Protocol.serializers import ProtocolosSerializer,SeccionesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from Protocol.models import ProtocolsModel
from rest_framework import serializers
from rest_framework.reverse import reverse


class FormatosReportesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='formato-reporte-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    protocolo = ProtocolosSerializer(many=True,read_only=True)
    protocolos_id = serializers.PrimaryKeyRelatedField(
        source='protocolo',
        write_only=True,
        many=True,
        queryset=ProtocolsModel.objects.filter(is_enabled = True))
    secciones = SeccionesSerializer(many=True,read_only=True)
    secciones_id = serializers.PrimaryKeyRelatedField(
        source="secciones",
        write_only=True,
        many=True,
        queryset=SeccionesModel.objects.filter(is_enabled = True))
    calculo = PruebaCalculoSerializer(many=True,read_only=True)
    calculos_id = serializers.PrimaryKeyRelatedField(
        source="calculo",
        write_only=True,
        many=True,
        queryset=PruebaCalculoModel.objects.filter(is_enabled = True))
    opcion = PruebaOpcionesSerializer(many=True,read_only=True)
    opciones_id = serializers.PrimaryKeyRelatedField(
        source="opcion",
        write_only=True,
        many=True,
        queryset=PruebaOpcionesModel.objects.filter(is_enabled = True))
    # variables = VariablesSerializer(many=True,read_only=True)
    # variables_id = serializers.PrimaryKeyRelatedField(
    #     source="variables",
    #     write_only=True,
    #     many=True,
    #     queryset=VariablesModel.objects.filter(is_enabled = True))
    class Meta:
        model = ReportsFormatsModel
        fields = (
            "id",
            "codigo_formato",
            "nombre_formato",
            "protocolo",
            "secciones",
            "calculo",
            "opcion",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "protocolos_id",
            "secciones_id",
            "calculos_id",
            "opciones_id")
   
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('formato-reporte-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('formato-reporte-delete',kwargs={"pk":obj.id},request=request)


class CategoriaReportesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='categoria-reporte-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    members = FormatosReportesSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=ReportsFormatsModel.objects.filter(is_enabled = True))

    class Meta:
        model = ReportsCategoryModel
        fields = (
            "id",
            "nombre_categoria",
            "abreviatura_categoria",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "members",
            "members_ids")
    
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('categoria-reporte-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('categoria-reporte-delete',kwargs={"pk":obj.id},request=request)

class ReporteReportesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='reporte-reporte-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    area = ProtocolosSerializer(many=True,read_only=True)
    areas_id = serializers.PrimaryKeyRelatedField(
        source='area',
        write_only=True,
        many=True,
        queryset=AreasModel.objects.filter(is_enabled = True))

    departamentos = ProtocolosSerializer(many=True,read_only=True)
    departamentos_id = serializers.PrimaryKeyRelatedField(
        source='departamentos',
        write_only=True,
        many=True,
        queryset=DepartamentoModel.objects.filter(is_enabled = True))

    organizacion = ProtocolosSerializer(many=True,read_only=True)
    organizacion_id = serializers.PrimaryKeyRelatedField(
        source='organizacion',
        write_only=True,
        many=True,
        queryset=OrganizacionModel.objects.filter(is_enabled = True))

    sistema = ProtocolosSerializer(many=True,read_only=True)
    sistema_id = serializers.PrimaryKeyRelatedField(
        source='sistema',
        write_only=True,
        many=True,
        queryset=SistemaModel.objects.filter(is_enabled = True))

    tubo = ProtocolosSerializer(many=True,read_only=True)
    tubo_id = serializers.PrimaryKeyRelatedField(
        source='tubo',
        write_only=True,
        many=True,
        queryset=TuboModel.objects.filter(is_enabled = True))

    machine = ProtocolosSerializer(many=True,read_only=True)
    machine_id = serializers.PrimaryKeyRelatedField(
        source='machine',
        write_only=True,
        many=True,
        queryset=MedidoresModel.objects.filter(is_enabled = True))

    formato = ProtocolosSerializer(many=True,read_only=True)
    formato_id = serializers.PrimaryKeyRelatedField(
        source='formato',
        write_only=True,
        many=True,
        queryset=ReportsFormatsModel.objects.filter(is_enabled = True))

    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "fecha_control_calidad",
            "numero_de_ot",
            "valores_operaciones",
            "area",
            "departamentos",
            "organizacion",
            "sistema",
            "tubo",
            "machine",
            "formato",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "areas_id",
            "departamentos_id",
            "organizacion_id",
            "sistema_id",
            "tubo_id",
            "machine_id",
            "formato_id")

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('reporte-reporte-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('reporte-reporte-delete',kwargs={"pk":obj.id},request=request)
