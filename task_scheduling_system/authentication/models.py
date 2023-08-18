# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField

from task_scheduling_system.authentication.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = EmailField("Email address", unique=True)
    full_name = CharField("Name of User", max_length=255)
    username = CharField("Username", max_length=64, unique=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
