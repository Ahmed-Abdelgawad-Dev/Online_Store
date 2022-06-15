from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user', 'name', 'paymentMethod', 'taxPrice', 'totalPrice', 'isPaid',
                    'paidAt', 'isDelivered', 'deliveredAt',)
    list_filter = ('_id', 'user', 'name', 'paymentMethod', 'taxPrice', 'totalPrice', 'isPaid',
                   'paidAt', 'isDelivered', 'deliveredAt',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user', 'name', 'product',
                    'order', 'quantity', 'price',)
    list_filter = ('_id', 'user', 'name', 'product',
                   'order', 'quantity', 'price',)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user', 'address',
                    'city', 'postalCode', 'country', 'telephone', 'shippingPrice',)
    list_filter = ('_id', 'user', 'address',
                   'city', 'postalCode', 'country', 'telephone', 'shippingPrice',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
