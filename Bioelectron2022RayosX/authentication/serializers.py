from rest_framework import serializers
from rest_framework import status
from rest_framework_simplejwt.tokens import TokenError,RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.utils import timezone
from .models import SesionesModel
from User.serializer import CustomUserSerializer

class LogoutSerializer(serializers.Serializer):
    refresh =serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
            # access_token = OutstandingToken.objects.filter(token=self.token)
            # access_token[0].expires_at = timezone.now()
            # access_token[0].save()
        except TokenError:
            return self.fail('bad_token')


class SesionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='sesiones-details',lookup_field='pk')
    user = CustomUserSerializer(read_only=True)
    ubicacion = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = SesionesModel
        fields = (
            'id',
            'user',
            'ubicacion',
            'is_enabled',
            'created_at',
            'url'
        )
    
    def get_ubicacion(self,obj):
        latitud = ''
        longitud = ''
        if(obj.ubicacion==None):
            return {'latitud':latitud,'longitud':longitud}
        else:
            return {'latitud':obj.ubicacion['latitud'],'longitud':obj.ubicacion['longitud']}
