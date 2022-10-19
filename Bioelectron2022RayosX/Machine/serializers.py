from .models import TuboModel,SistemaModel
from rest_framework import serializers
from rest_framework.reverse import reverse

class TuboSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tubo-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = TuboModel
        fields = ('id','title','name_option','marca','modelo','serie','antiguedad','year_instalacion','is_enabled','created_at','url','edit_url','delete_url')
        

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


class SistemaSerializer(serializers.ModelSerializer):
    members = TuboSerializer(many=True,read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(
        source='members',
        write_only=True,
        many=True,
        queryset=TuboModel.objects.filter(is_enabled = True))
    url = serializers.HyperlinkedIdentityField(view_name='sistema-detail',lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only = True)
    delete_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = SistemaModel
        fields = ('id','marca','modelo','name_option','serie','antiguedad','year_instalacion','is_enabled','created_at','url','edit_url','delete_url','members','members_ids')
        

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
    
    def update(self, instance, validated_data):
        if 'members' in validated_data:
            instance.members.set(validated_data['members'])
        instance.save()
        return instance