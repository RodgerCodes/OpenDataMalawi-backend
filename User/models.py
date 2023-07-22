from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as d

from User.manager import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=500)
    email = models.EmailField(unique=True, max_length=500)
    password = models.CharField(max_length=10000)
    is_staff = models.BooleanField(
        d("staff status"),
        default=False,
        help_text=d("Designates whether the user can log into this admin site."),
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class VerificationCodes(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_code = models.PositiveIntegerField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userID.email
