from .models import Product
from django.conf import settings
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        # fields = ('_id', 'user', 'name', 'brand', ' images', 'description',
        #           'rating', 'reviewsCount', 'price', 'stockCount', 'created', 'updated',)
        fields = '__all__'
