from asyncio.windows_events import NULL
from dataclasses import fields
from pyexpat import model
from Operations.models import VariablesModel
from Operations.serializers import VariablesSerializer
from CompanyMachine.models import MedidoresModel
from Machine.models import SistemaModel, TuboModel
from Customer.models import AreasModel,DepartamentoModel,OrganizacionModel
from .models import ReportsCategoryModel, ReportsFormatsModel,PruebaCalculoModel,PruebaOpcionesModel, ReportsReporteModel, Rpt_Varr_Model,SeccionesModel
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
    variables = serializers.SerializerMethodField(read_only = True)
    variables_formato_ids = serializers.PrimaryKeyRelatedField(
        source="variables_formato",
        write_only=True,
        many=True,
        queryset=VariablesModel.objects.filter(is_enabled = True))
        
    class Meta:
        model = ReportsFormatsModel
        fields = (
            "id",
            "codigo_formato",
            "nombre_formato",
            "protocolo",
            "secciones",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "protocolos_id",
            "secciones_id",
            "variables",
            "variables_formato_ids")
    
    def get_variables(self,obj):
        request = Rpt_Varr_Model.objects.filter(formato = obj.id)
        Uc = []
        for x in request:
            print(x.variable!=NULL)
            if(x.variable):
                Uc.append(
                    {
                        "id":x.id,
                        "posicion":x.posicion,
                        "sub_posicion":x.sub_posicion,
                        "identificador_variable":x.variable.id,
                        "nombre_variable":x.variable.nombre_variable,
                        "range":x.variable.range_variable,
                        "valor":x.variable.valor_defecto
                    }
                )
            else:
                Uc.append(
                    {
                        "id":x.id,
                        "posicion":x.posicion,
                        "sub_posicion":x.sub_posicion,
                        "nombre_categoria":x.subtitle_posicion,
                    }
                )
        # print(self)
        return Uc
   
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
            "numero_de_ot",
            "fecha_control_calidad",
            "datos_del_cliente",
            "sistema",
            "componente",
            "machine",
            "valores_operaciones",
            "formato",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
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
