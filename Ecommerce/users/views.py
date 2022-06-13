from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserSerializerWithToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serialized_user = CustomUserSerializer(user, many=False)
    return Response(serialized_user.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = CustomUser.objects.all()
    serialized_users = CustomUserSerializer(users, many=True)
    return Response(serialized_users.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serialized_user = CustomUserSerializerWithToken(self.user).data
        for key, value in serialized_user.items():
            data[key] = value
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
