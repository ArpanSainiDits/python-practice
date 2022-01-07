import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields import BigAutoField
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    email_verify = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField('active', default=False)
    is_superuser = models.BooleanField(default=True)
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

    registerotp = models.IntegerField()
    
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)


class task(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=200)
    due_date = models.DateField()
    status = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    User = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)