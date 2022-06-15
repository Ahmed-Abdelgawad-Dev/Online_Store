
from .models import Order, ShippingAddress
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework.status import HTTP_404_NOT_FOUND


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# To be completed later
def add_order_items(request):
    user = request.user
    data = request.data
    order_items = data['order_items']
    if order_items is not None and len(order_items) < 1:
        return Response({"Attention": "You have not any order item yet"}, status=HTTP_404_NOT_FOUND)
    else:
        # Created Order
        created_order = Order.objects.create(
            name=data['name'],
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            totalPrice=data['totalPrice'],
            isPaid=data['isPaid'],
            isDelivered=data['isDelivered'],
            deliveredAt=data['deliveredAt']
        )
        # Created Shipping Adress.
        shipping_data = data['shipping_address']
        ShippingAddress.objects.create(
            name=data['name'],
            user=user,
            order=created_order,
            address=shipping_data['adress'],
            city=shipping_data['city'],
            postalCode=shipping_data['postalCode'],
            country=shipping_data['country'],
            shippingPrice=shipping_data['shippingPrice'],
            telephone=shipping_data['shippingPrice']
        )
