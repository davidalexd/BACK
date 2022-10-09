from .models import ReportsCategoryModel, ReportsFormatsModel,VariablesModel,PruebaCalculoModel,PruebaOpcionesModel,SeccionesModel
from Protocol.serializers import ProtocolosSerializer,VariablesSerializer,SeccionesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from Protocol.models import ProtocolsModel
from rest_framework import serializers
from rest_framework.reverse import reverse


class FormatosReportesSerializer(serializers.ModelSerializer):
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
        fields = ("id","codigo_formato","nombre_formato","protocolo","secciones","calculo","opcion","is_enabled","created_at","protocolos_id","secciones_id","calculos_id","opciones_id")

class CategoriaReportesSerializer(serializers.ModelSerializer):
    members = FormatosReportesSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=ReportsFormatsModel.objects.filter(is_enabled = True))
    class Meta:
        model = ReportsCategoryModel
        fields = ("id","nombre_categoria","abreviatura_categoria","is_enabled","created_at","members","members_ids")
