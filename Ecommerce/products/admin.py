from django.contrib import admin
from .models import Product, Review, ProductThumbnails


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'user', 'product', 'rating', 'comment',)
    list_filter = ('_id', 'name', 'user', 'product', 'rating', 'comment',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
