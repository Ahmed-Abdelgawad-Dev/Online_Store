from django.contrib import admin
from .models import Product, Order, OrderItem, Review, ShippingAddress, Thumbnails


class ThumbnailsAdmin(admin.StackedInline):
    model = Thumbnails


class ProductAdmin(admin.ModelAdmin):
    inlines = [ThumbnailsAdmin]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register([Order, OrderItem, Review,
                    ShippingAddress, Thumbnails])
