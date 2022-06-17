from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from products.models import Product
from .models import Order, OrderItem, ShippingAddress
from .serializers import OrderSerializer
from rest_framework import status
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'details': 'Noo Items yet'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Instanciate an order.
        order = Order.objects.create(
            name="ahmed",
            user=user,
            paymentMethod=data['paymentMethod'],
            # taxPrice=data['taxPrice'],
            # shippingPrice=data['shippingPrice'],
            # totalPrice=data['totalPrice']
        )
        # Instanciate shipping address
        shipping = ShippingAddress.objects.create(
            name="order",
            user=user,
            order=order,
            # address=data['shippingAddress']['address'],
            # city=data['shippingAddress']['city'],
            # postalCode=data['shippingAddress']['postalCode'],
            # country=data['shippingAddress']['country'],
        )

        # link the orderItem with its order.
        for i in orderItems:
            product = Product.objects.get(_id=i['product'])

            item = OrderItem.objects.create(
                name=product.name,
                product=product,
                order=order,
                # quantity=i['quantity'],
                # price=i['price'],
                # image=product.image.url,
            )
            # Change the stock count
            product.stockCount -= item.quantity
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response({'Attention': "Sorry, you can't view this order"},
                     status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'Attention': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(_id=pk)

    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()

    return Response('Order paid')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(_id=pk)

    order.isDelivered = True
    order.deliveredAt = datetime.now()
    order.save()

    return Response('Order delivered')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(_id=pk)

    order.isDelivered = True
    order.deliveredAt = datetime.now()
    order.save()

    return Response('Order was delivered')
