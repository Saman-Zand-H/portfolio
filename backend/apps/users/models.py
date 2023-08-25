from uuid import uuid4
from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)

from .enums import Genders


class UserModel(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        default=uuid4, auto_created=True, unique=True, editable=False
    )
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(
        choices=Genders.choices, max_length=1, default=Genders.just_stupid, blank=True
    )
    picture = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name_plural = "UserModel"

    @cached_property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"@{self.username} - {self.name}"
