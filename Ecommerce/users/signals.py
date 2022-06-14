from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save, sender=CustomUser)
def auto_rename_user(sender, instance, **kwargs):
    user = instance
    """ Extract a name from the email in case user has no name Ex.xyz@gmail => name=xyz """
    if user.name == '':
        user.name = user.email.split("@")[0]
