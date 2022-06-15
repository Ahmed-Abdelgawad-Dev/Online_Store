from PIL import Image
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
"""
- Some fields are camelCase as per Front-end team request

- An abstract model to inherit from i/of DRY"""


class BaseAbstractModel(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Product(BaseAbstractModel):
    brand = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    images = models.ImageField(blank=True)
    description = models.TextField(max_length=150)

    rating = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    reviewsCount = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    featured = models.BooleanField(default=False)
    freeShipping = models.BooleanField(default=False)
    onSale = models.BooleanField(default=False)
    saleNumber = models.IntegerField(default=0, validators=[
        MaxValueValidator(100000000000000000000000000000000),
        MinValueValidator(0)
    ])
    stockCount = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Thumbnails(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Thumbnails')
    photo = models.ImageField()

    # Resizing the Thumbnals' images to fit the standards | Requirements
    def save(self, *args, **kwargs):
        super(Thumbnails, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((370, 370))
        img.save(self.photo.path, quality=70, optimize=True)

    def __str__(self):
        return str(self.product.name)


class Review(BaseAbstractModel):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.rating)


class Order(BaseAbstractModel):
    paymentMethod = models.CharField(max_length=100)
    taxPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ['-created']


class OrderItem(BaseAbstractModel):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ShippingAddress(BaseAbstractModel):
    order = models.OneToOneField(Order,
                                 on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postalCode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    telephone = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.address)
