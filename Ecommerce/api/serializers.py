from .models import Product
from django.conf import settings
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        """__all__ is not recommended in general for a security reason but we can use it with the product | but not with users 4example"""
        fields = '__all__'
        # fields = ('_id', 'user', 'name', 'brand', ' images', 'description',
        #           'rating', 'reviewsCount', 'price', 'stockCount', 'created', 'updated',)
