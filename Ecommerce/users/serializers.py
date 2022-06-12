from rest_framework import serializers
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email',  'name', 'is_staff',
                  'isAdmin', 'is_active', '_id',)

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff


class CustomUserSerializerWithToken(CustomUserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email',  'name', 'is_staff',
                  'isAdmin', 'is_active', '_id', 'token',)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
