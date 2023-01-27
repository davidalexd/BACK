from django.contrib.auth import authenticate
from rest_framework import status,permissions
from rest_framework.response import Response
from .serializers import LogoutSerializer,SesionSerializer
from .models import SesionesModel
from authentication.mixins import StaffEditorPermissionMixin
from rest_framework import generics
from rest_framework.exceptions import APIException,status
from rest_framework_simplejwt.views import TokenObtainPairView
from User.serializer import CustomTokenObtainPairSerializer, CustomUserSerializer

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        ubicacion = request.data.get('ubicacion', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():

                user_serializer = CustomUserSerializer(user)

                json_ubicacion = ({
                    'ubicacion':{'latitud':ubicacion['latitud'],'longitud':ubicacion['longitud']},
                    'user':user_serializer.data['id']
                    })
                user_ubicacion = SesionSerializer(data=json_ubicacion)
                user_ubicacion.is_valid(raise_exception=True)
                user_ubicacion.save()

                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

class Logout(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)

class Sesiones(StaffEditorPermissionMixin,generics.ListAPIView):
    serializer_class = SesionSerializer    
    def get_queryset(self):     
        queryset = SesionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
class SesionesByID(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = SesionSerializer   
    lookup_field = 'pk' 
    def get_queryset(self):     
        queryset = SesionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No se encontraron registros', })

