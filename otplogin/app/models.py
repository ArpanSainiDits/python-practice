import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields import BigAutoField
from django.utils import timezone

from .managers import CustomUserManager


class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # Roles created here
    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class otpVerify(models.Model):

    otp = models.IntegerField()
   
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)


