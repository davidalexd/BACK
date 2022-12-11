from rest_framework import status, authentication, exceptions
from rest_framework.authentication import get_authorization_header
from .authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAdminUser
from authentication.permissions import IsStaffEditorPermission

# from rest_framework import permissions

class StaffEditorPermissionMixin(authentication.BaseAuthentication):
    user = None
    permission_classes = [IsAdminUser,IsStaffEditorPermission]
    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None            
            token_expire = ExpiringTokenAuthentication()

            user = token_expire.authenticate_credentials(token)
            if user != None:
                self.user = user
                return user
        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')

        return (self.user, 1)