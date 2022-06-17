from django.urls import path
from . import views


urlpatterns = [

    path('', views.getOrders, name='orders'),
    path('add_order/', views.addOrderItems, name='add-order'),
    path('my_orders/', views.getMyOrders, name='my-orders'),
    path('<str:pk>/delivered/', views.updateOrderToDelivered, name='order-delivered'),

    path('<str:pk>/', views.getOrderById, name='get-order'),
    path('<str:pk>/paid/', views.updateOrderToPaid, name='pay'),
]
