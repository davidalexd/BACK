from .models import OperacionesModel
from rest_framework import serializers
from rest_framework.reverse import reverse

class OperacionesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='operacion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = OperacionesModel
        fields = ('id','operacion_titulo','operacion_funcion',"operacion_variable",'operacion_symbol','operacion_contexto','is_enabled','created_at','url','edit_url','delete_url')
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('operacion-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('operacion-delete',kwargs={"pk":obj.id},request=request)
