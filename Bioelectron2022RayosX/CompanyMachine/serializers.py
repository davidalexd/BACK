from rest_framework import serializers
from .models import MedidoresModel,CalibracionesModel
from rest_framework.reverse import reverse

class CalibracionesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='calibracion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = CalibracionesModel
        fields = ('id','fecha_calibracion','is_enabled','created_at','url','edit_url','delete_url')
    
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

class MedidoresSerializer(serializers.ModelSerializer):
    members = CalibracionesSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=CalibracionesModel.objects.filter(is_enabled = True))
    url = serializers.HyperlinkedIdentityField(view_name='medidor-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = MedidoresModel
        fields = ('id','title','marca','full_name','modelo','serie','is_enabled','created_at','url','edit_url','delete_url','members','members_ids')
    
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
