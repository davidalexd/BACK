from rest_framework import serializers
from .models import MedidoresModel,CalibracionesModel,User_Medidores_Model,User_Calibraciones_Model
from rest_framework.reverse import reverse

class CalibracionesSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='calibracion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = CalibracionesModel
        fields = ('id','fecha_calibracion','is_enabled','created_at','url','edit_url','delete_url','actions')
    
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('calibracion-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None 
        return reverse('calibracion-delete',kwargs={"pk":obj.id},request=request)
    
    def get_actions(self,obj):
        Uc = []
        autores = User_Calibraciones_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autores":x.model_user.username,
                "email":x.model_user.email,
                "calibracion":x.model.fecha_calibracion,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc

class MedidoresSerializer(serializers.ModelSerializer):
    members = CalibracionesSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=CalibracionesModel.objects.filter(is_enabled = True))
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='medidor-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = MedidoresModel
        fields = ('id','marca','modelo','serie','is_enabled','created_at','url','edit_url','delete_url','members','actions','members_ids')
    
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('medidor-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None 
        return reverse('medidor-delete',kwargs={"pk":obj.id},request=request)
    
    def get_actions(self,obj):
        Uc = []
        autores = User_Medidores_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autores":x.model_user.username,
                "email":x.model_user.email,
                "calibracion":x.model.full_name,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc


class UserCalibracionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Calibraciones_Model
        fields = '__all__'

class UserMedidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Medidores_Model
        fields = '__all__'