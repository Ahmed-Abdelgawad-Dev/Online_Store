from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email',
                  'is_superuser', 'is_active', ]
