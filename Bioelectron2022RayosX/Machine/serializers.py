from .models import TuboModel,SistemaModel,User_sistemas_Model,User_tubos_Model
from rest_framework import serializers
from rest_framework.reverse import reverse

class TuboSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='tubo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = TuboModel
        fields = ('id','marca','modelo','serie','antiguedad','year_instalacion','is_enabled','created_at','url','edit_url','delete_url','actions')
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('tubo-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('tubo-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_tubos_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.marca,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc


class SistemaSerializer(serializers.ModelSerializer):
    members = TuboSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=TuboModel.objects.filter(is_enabled = True))
    actions = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='sistema-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = SistemaModel
        fields = ('id','marca','modelo','serie','antiguedad','year_instalacion','is_enabled','created_at','url','edit_url','delete_url','members','actions','members_ids')
        

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('sistema-update',kwargs={"pk":obj.id},request=request)

    def get_delete_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('sistema-delete',kwargs={"pk":obj.id},request=request)

    def get_actions(self,obj):
        Uc = []
        autores = User_sistemas_Model.objects.filter(model=obj.id)
        for x in autores:
            Uc.append({
                "autor":x.model_user.username,
                "email":x.model_user.email,
                "area":x.model.marca,
                "context":x.context,
                "registered_at":x.registerd_at
            })
        return Uc
    
    def update(self, instance, validated_data):
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        instance.save()
        return instance

class UsersistemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_sistemas_Model
        fields = '__all__'

class UserTubosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_tubos_Model
        fields = '__all__'
        