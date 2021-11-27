from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Model manager without a username field"""
    use_in_migrations = True

    def _create_user(self, email, password, **rest):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Please set an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **rest)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **rest):
        """Create and save a regular User with the given email and password."""
        rest.setdefault('is_staff', False)
        rest.setdefault('is_superuser', False)
        return self._create_user(email, password, **rest)

    def create_superuser(self, email, password, **rest):
        """Create and save a SuperUser with the given email and password."""
        rest.setdefault('is_staff', True)
        rest.setdefault('is_superuser', True)

        if rest.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if rest.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **rest)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
