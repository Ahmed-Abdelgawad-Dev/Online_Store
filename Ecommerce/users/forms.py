from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = ('email', 'name',)
        """__all__ will be changed later for security reasons"""
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = ('email', 'name',)
        """__all__ will be changed later for security reasons"""
        fields = '__all__'
