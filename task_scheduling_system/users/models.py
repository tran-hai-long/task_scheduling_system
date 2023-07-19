from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    email = EmailField("Email address", unique=True)
    full_name = CharField("Name of User", blank=True, max_length=255)
    username = CharField("Username", max_length=64, unique=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
