from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view()
def info(request):
    return Response({"Info": "All Entities"})


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
