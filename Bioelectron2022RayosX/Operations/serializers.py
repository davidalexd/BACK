from .models import OperacionesModel, User_Operaciones_Model
from rest_framework import serializers
from rest_framework.reverse import reverse

class OperacionesSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='operacion-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = OperacionesModel
        fields = ('id','operacion_titulo','operacion_funcion','operacion_symbol','operacion_contexto','is_enabled','created_at','url','edit_url','delete_url','actions')
        

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

    def get_actions(self,obj):
        Uc = []
        autores = User_Operaciones_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.operacion_titulo,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc


class UserOperacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Operaciones_Model
        fields = '__all__'