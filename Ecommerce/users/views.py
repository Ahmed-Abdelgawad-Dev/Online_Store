from urllib import response
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserSerializerWithToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework.status import HTTP_404_NOT_FOUND


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


@api_view(['POST'])
def register_user(request):
    user_data = request.data
    try:
        created_user = CustomUser.objects.create(
            email=user_data['email'],
            name=user_data['name'],
            password=make_password(user_data['password'])
        )

        serialized_user = CustomUserSerializerWithToken(
            created_user, many=False)
        return Response(serialized_user.data)
    except:
        return Response({"Attention": "The username is already existed, please choose a nother username"}, HTTP_404_NOT_FOUND)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serialized_user = CustomUserSerializerWithToken(self.user).data
        for key, value in serialized_user.items():
            data[key] = value
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
