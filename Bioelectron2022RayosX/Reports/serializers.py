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
from datetime import timedelta
from rest_framework.reverse import reverse
from User.serializer import CustomAuthorSerializer
from User.models import User
from django.contrib.sites.shortcuts import get_current_site

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
            "variables",
            "secciones",
            "is_enabled",
            "created_at",
            "url",
            "edit_url",
            "delete_url",
            "protocolos_id",
            "secciones_id",
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
                rv = []
                for r in range(x.variable.range_variable):

                    rv.append({
                        'name':str(r+1)+'-'+str(x.variable.nombre_variable)+'-'+str(x.variable.id),
                        'valor_defecto':"Null",
                        'valor_opciones':x.variable.valor_defecto
                    })

                Uc.append(
                    {
                        "id":x.id,
                        "posicion":x.posicion,
                        "sub_posicion":x.sub_posicion,
                        "identificador_variable":x.variable.id,
                        "nombre_variable":x.variable.nombre_variable,
                        "range":rv,
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


class sHistory(serializers.ModelSerializer):
    def __init__(self, model, *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass

class ReporteReportesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='reporte-reporte-detail',lookup_field='pk')    
    autor = serializers.SerializerMethodField(read_only = True) 
    gerente = serializers.SerializerMethodField(read_only = True)
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
            "autor",
            "gerente",
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
            "certificado_url"
            )

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
        else:
            if obj.certificado.is_enabled is True:
                return {'message':'Certificado Aprobado','data':reverse('certificado-reporte-detail',kwargs={"pk":obj.certificado.id},request=request),'status':True}
            else:
                return {'message':'Certificado Desaprobado','data':reverse('certificado-reporte-detail',kwargs={"pk":obj.certificado.id},request=request),'status':True}
    @property
    def base_url(self):
        return "http://" + get_current_site(self.context.get('request')).domain
    
    def get_autor(self, obj):
        try:
            model = obj.historical.__dict__['model']
            fields = '__all__'
            serializer = sHistory(model, obj.historical.all(), fields=fields, many=True)
            serializer.is_valid()
            author = User.objects.get(id=serializer.data[0]['history_user'])
            usuario =  CustomAuthorSerializer(author).data
            return {"autor_numero":usuario['numero'],"autor_nombre":usuario['name'],"autor_apellido":usuario['last_name'],"autor_firma":self.base_url+usuario['firma']}
        except Exception as e:
            author = User.objects.get(id=2)
            usuario =  CustomAuthorSerializer(author).data
            return {"autor_numero":usuario['numero'],"autor_nombre":usuario['name'],"autor_apellido":usuario['last_name'],"autor_firma":self.base_url+usuario['firma']}

        

    def get_gerente(self, obj):
        try:
            model = obj.historical.__dict__['model']
            fields = '__all__'
            serializer = sHistory(model, obj.historical.all(), fields=fields, many=True)
            serializer.is_valid()
            author = User.objects.get(id=3)
            usuario =  CustomAuthorSerializer(author).data
            return {"gerente_numero":usuario['numero'],"gerente_nombre":usuario['name'],"gerente_apellido":usuario['last_name'],"gerente_firma":self.base_url+usuario['firma']}
        except Exception as e:
            return {"gerente_numero":"","gerente_nombre":"","gerente_apellido":"","gerente_firma":""}
    

def json_respuestas(data):
    return False == data[0]['resultados'][0]['resultados']['resultado']['estado']

class CertificadoReportesSerializer(serializers.ModelSerializer):
    InformeID = serializers.IntegerField(write_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='certificado-reporte-detail',lookup_field='pk')   
    detalles = serializers.SerializerMethodField(read_only = True)     

    def get_detalles(self,obj):
        if obj.is_enabled == True:
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
        else:
            data = None
    
    class Meta:
        model = ReportsCertificadoModel
        fields = (
            'id',            
            'detalles',
            'created_at',
            'url',
            'InformeID',
        )


    def create(self, validated_data):
        informe = validated_data['InformeID']       
        
        obj = ReportsReporteModel.objects.get(id=informe)
        if obj.certificado is None:
            Uc = list(filter(json_respuestas,obj.pruebas[1]))
            if(len(Uc)>0):
                status = False
            else:
                status = True
            certificado = ReportsCertificadoModel.objects.create(is_enabled=status)


            obj.certificado = certificado
            obj.is_enabled = True
            obj.save()  
            return certificado
        else:
            return obj.certificado




class ReporteReportesClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "numero_de_ot",
            "fecha_control_calidad",
            "observacion",
            "datos_del_cliente",
        )
    
    # def update(self, instance, validated_data): 
    #     instance.numero_de_ot =  validated_data['numero_de_ot'],
    #     instance.observacion = validated_data['observacion'],       
    #     instance.fecha_control_calidad = validated_data['fecha_control_calidad'],
    #     instance.datos_del_cliente = {
    #         "razon_social":validated_data['datos_del_cliente']['razon_social'],
    #         "ruc":validated_data['datos_del_cliente']['ruc'],
    #         "direccion":validated_data['datos_del_cliente']['direccion'],
    #         "distrito":validated_data['datos_del_cliente']['distrito'],
    #         "provincia":validated_data['datos_del_cliente']['provincia'],
    #         "region":validated_data['datos_del_cliente']['region'],
    #         "contactos": instance.datos_del_cliente['contactos'],
    #         "instalacion_direccion":validated_data['datos_del_cliente']['instalacion_direccion'],
    #         "instalacion_distrito":validated_data['datos_del_cliente']['instalacion_distrito'],
    #         "instalacion_provincia":validated_data['datos_del_cliente']['instalacion_provincia'],
    #         "instalacion_region":validated_data['datos_del_cliente']['instalacion_region'],
    #         "instalacion_ambiente":validated_data['datos_del_cliente']['instalacion_ambiente'],
    #     }     
    #     instance.save()
    #     return instance

class ReporteReportesSistemaControlCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "sistema",
            "componente",
        )

class ReporteReportesMaquinaControlCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "machine"
        )


class ReporteReportesOpcionesSerializer(serializers.ModelSerializer):
    opciones_pruebas = serializers.SerializerMethodField(read_only = True)
    opciones = serializers.JSONField(write_only=True)
    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "opciones_pruebas",
            "opciones"
        )

    def update(self, instance, validated_data):
        opciones = instance.pruebas[0]
        for x in range(len(validated_data['opciones'])):
            opciones[x]['valor'] = validated_data['opciones'][x]
        instance.save()        
        return instance

    def get_opciones_pruebas(self,obj):
        return obj.pruebas[0]


class ReporteReportesPruebasSerializer(serializers.ModelSerializer):
    operaciones_pruebas = serializers.SerializerMethodField(read_only = True)
    posicion = serializers.IntegerField(write_only=True)
    criterio = serializers.JSONField(write_only=True)
    class Meta:
        model = ReportsReporteModel
        fields = (
            "id",
            "operaciones_pruebas",
            "posicion",
            "criterio",
        )

    def update(self, instance, validated_data):
        operaciones = instance.pruebas[1]
        posición_operador =  operaciones[validated_data['posicion']][0]['resultados'][0]['resultados']['resultado']

        for x in range(len(validated_data['criterio'])):
            posición_operador['data'][x]['resultado'] = validated_data['criterio'][x]
            posición_operador['data'][x]['estado'] = True
        
        if (len(validated_data['criterio']) == len(posición_operador['data'])):
            posición_operador['estado'] = True

        instance.save()
        return instance

    
    def get_operaciones_pruebas(self,obj):
        return obj.pruebas[1]
    

        

