from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from products.models import BaseAbstractModel, Product


class Order(BaseAbstractModel):
    class PaymentChoices(models.TextChoices):
        ON_DELIVERY = 'ON_DELIVERY', _('ON_DELIVERY')
        VISA = 'VISA', _('VISA')
        MASTER_CARD = 'MASTER_CARD', _('MASTER_CARD')
        MAESTRO = 'MAESTRO', _('MAESTRO')
        AMEX = 'AMEX', _('AMEX')
        PAYPAL = 'PAYPAL', _('PAYPAL')
    paymentMethod = models.CharField(
        max_length=50, choices=PaymentChoices.choices,
        default=PaymentChoices.ON_DELIVERY,)
    taxPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return ("%s's order" % (self.user.name).upper())

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
        return str("{}'s {}".format(self.user.name, self.order.name))

    class Meta:
        ordering = ['-created']


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
