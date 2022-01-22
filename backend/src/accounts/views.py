from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .models import MyUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
