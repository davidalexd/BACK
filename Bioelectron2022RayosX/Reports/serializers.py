from urllib import request
from Operations.models import VariablesModel
from Operations.serializers import VariablesSerializer
from CompanyMachine.models import MedidoresModel
from Machine.models import SistemaModel, TuboModel
from Customer.models import AreasModel,DepartamentoModel,OrganizacionModel
from .models import Frt_Cat_Model, ReportsCategoryModel, ReportsFormatsModel,PruebaCalculoModel,PruebaOpcionesModel, ReportsReporteModel, Rpt_Prt_Model, Rpt_Varr_Model,SeccionesModel,ReportsCertificadoModel
from Protocol.serializers import ProtocolosSerializer,SeccionesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from Protocol.models import ProtocolsModel
from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import timedelta
from datetime import datetime

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
    certificado_url = serializers.SerializerMethodField(read_only = True)

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
            "title_image_1",
            "title_image_2",
            "title_image_3",
            "image_1",
            "image_2",
            "image_3",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "formato_id",
            "certificado_url")

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
    
    def get_certificado_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        if obj.certificado is None:
            return {'message':'Informe no evaluado','data':None,'status':False}
        return {'message':'Certificado Aprobado','data':reverse('certificado-reporte-detail',kwargs={"pk":obj.certificado.id},request=request),'status':True}


class CertificadoReportesSerializer(serializers.ModelSerializer):
    InformeID = serializers.IntegerField(write_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='certificado-reporte-detail',lookup_field='pk')   
    detalles = serializers.SerializerMethodField(read_only = True)     

    def get_detalles(self,obj):
        request = ReportsReporteModel.objects.get(certificado = obj.id)
        data = {
            "certificado": "Certificado Nº " + str(obj.id)+"-BIO",
            "informe":"Informe Nº"+str(request.id)+"-"+str(request.nombre_reporte),
            "fecha_control_calidad":request.fecha_control_calidad,
            "ubicacion":request.datos_del_cliente['instalacion_direccion']+","+request.datos_del_cliente['instalacion_distrito']+","+request.datos_del_cliente['instalacion_provincia']+","+request.datos_del_cliente['instalacion_region']+","+request.datos_del_cliente['instalacion_ambiente'],
            "vigencia":"Válido hasta el "+str(request.fecha_control_calidad+timedelta(days=360))+" o hasta que se realice un mantenimiento correctivo",
            "equipo":{"sistema":request.sistema,"componente":request.componente},
        }
        return data  
    
    class Meta:
        model = ReportsCertificadoModel
        fields = (
            'id',            
            'detalles',
            'is_enabled',
            'created_at',
            'url',
            'InformeID',
        )

    def create(self, validated_data):
        status = validated_data['is_enabled']
        informe = validated_data['InformeID']        
        certificado = ReportsCertificadoModel.objects.create(is_enabled=status)
        obj = ReportsReporteModel.objects.get(id=informe)
        obj.certificado = certificado
        obj.save()  
        return certificado   


