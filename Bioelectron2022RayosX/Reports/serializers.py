from urllib import request
from Operations.models import VariablesModel
from Operations.serializers import VariablesSerializer
from CompanyMachine.models import MedidoresModel
from Machine.models import SistemaModel, TuboModel
from Customer.models import AreasModel,DepartamentoModel,OrganizacionModel
from .models import Frt_Cat_Model, ReportsCategoryModel, ReportsFormatsModel,PruebaCalculoModel,PruebaOpcionesModel, ReportsReporteModel, Rpt_Prt_Model, Rpt_Varr_Model,SeccionesModel
from Protocol.serializers import ProtocolosSerializer,SeccionesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from Protocol.models import ProtocolsModel
from rest_framework import serializers
from rest_framework.reverse import reverse


class FormatosReportesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='formato-reporte-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    protocolo = serializers.SerializerMethodField(read_only = True)
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

    categorias = serializers.SerializerMethodField(read_only = True)
        
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
            "categorias",
            "variables_formato_ids")
    
    def get_categorias(self,obj):
        request = Frt_Cat_Model.objects.filter(formatos = obj.id)
        Uc = []
        for x in request:
                Uc.append(
                    {
                        "identificador":x.id,
                        "id":x.categoria.id,
                        "nombre_categoria":x.categoria.nombre_categoria,
                        "abreviatura_categoria":x.categoria.abreviatura_categoria,
                    }
                )
        return Uc
    def get_protocolo(self,obj):
        request = Rpt_Prt_Model.objects.filter(formato = obj.id)
        Uc = []
        for x in request:
                Uc.append(
                    {
                        "id":x.id,
                        "protocolo_detalles":x.protocolo_detalles,
                        "protocolo":x.protocolo.id,
                        "protocolo_titulo":x.protocolo.protocolo_titulo,
                    }
                )
        return Uc
    def get_variables(self,obj):
        request = Rpt_Varr_Model.objects.filter(formato = obj.id)
        Uc = []
        for x in request:
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

    formato = FormatosReportesSerializer(many=True,read_only=True)
    formato_id = serializers.PrimaryKeyRelatedField(
        source='formato',
        write_only=True,
        many=True,
        queryset=ReportsFormatsModel.objects.filter(is_enabled = True))

    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "nombre_reporte",
            "numero_de_ot",
            "fecha_control_calidad",
            "observacion",
            "datos_del_cliente",
            "sistema",
            "componente",
            "machine",
            "valores_operaciones",
            "formato",
            "pruebas",
            "image_1",
            "image_2",
            "image_3",
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
