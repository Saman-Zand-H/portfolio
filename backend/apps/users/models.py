from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.contrib.auth.models import (AbstractBaseUser, 
                                        Permission, 
                                        BaseUserManager)

from .enums import Genders


class UserManager(BaseUserManager):
    def _create_user(self,
                     username,
                     password,
                     email,
                     is_active,
                     is_staff,
                     is_superuser,
                     picture,
                     first_name,
                     last_name):
        normalized_email = None
        if bool(email):
            self.normalize_email(email)
        now = timezone.now()
        user = self.create(
            username=username,
            email=normalized_email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            picture=picture,
            first_name=first_name,
            last_name=last_name,
            date_joined=now
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,
                    username=None,
                    password=None,
                    email=None,
                    first_name=None,
                    last_name=None,
                    picture=None,
                    is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=False,
            is_staff=False
        )
    
    def create_staff(self,
                     username=None,
                     password=None,
                     email=None,
                     first_name=None,
                     last_name=None,
                     picture=None,
                     is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=False,
            is_staff=True
        )
    
    def create_superuser(self,
                         username=None,
                         password=None,
                         email=None,
                         first_name=None,
                         last_name=None,
                         picture=None,
                         is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=True,
            is_staff=True
        )


class UserModel(AbstractBaseUser, Permission):
    uuid = models.UUIDField(default=uuid4,
                            auto_created=True,
                            unique=True,
                            editable=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(
        choices=Genders.choices, 
        max_length=1, 
        default="U", 
        blank=True
    )
    picture = models.ImageField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    @cached_property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"@{self.username} - {self.name()}"
    