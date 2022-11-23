from rest_framework import serializers
from rest_framework import status
from rest_framework_simplejwt.tokens import TokenError,RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.utils import timezone

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
            # RefreshToken(self.token).blacklist()
            access_token = OutstandingToken.objects.filter(token=self.token)
            access_token[0].expires_at = timezone.now()
            access_token[0].save()
        except TokenError:
            return self.fail('bad_token')
            
