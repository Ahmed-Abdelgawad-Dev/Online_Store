from django.contrib import admin
from .models import Product, Order, OrderItem, Review, ShippingAddress, ProductThumbnails


class ProductThumbnailsAdmin(admin.StackedInline):
    model = ProductThumbnails


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductThumbnailsAdmin]
    list_display = ('name', 'price', 'rating', 'created',
                    'updated', 'stockCount', 'reviewsCount', 'featured', 'freeShipping', 'onSale',)
    list_filter = ('name', 'price', 'rating', 'stockCount',
                   'reviewsCount', 'featured', 'freeShipping', 'onSale',)

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register([Order, OrderItem, Review,
                    ShippingAddress])
