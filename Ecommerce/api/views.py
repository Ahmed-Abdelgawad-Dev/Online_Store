from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view()
def info(request):
    return Response({"/products": "Get all products", "/products": "Get one product"})


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(_id=pk)
    serialized_products = ProductSerializer(product, many=False)
    return Response(serialized_products.data)
