from django.db import models
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser


def validate_strong_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one number")
    if not re.search(r"[@$!%*?&]", password):
        raise ValidationError("Password must contain at least one special character (@, $, !, %, *, ?, &)")


class Registerlogin(AbstractBaseUser):
    ROLE_CHOICES = [
        ("manager", "Manager"),
        ("retailer", "Retailer"),
        ("admin", "Admin"),
        ("normal", "Normal"),
    ]
    last_login = None
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, choices=ROLE_CHOICES)
    password = models.CharField(
        max_length=128,
        validators=[validate_strong_password]
    )
    permission = models.TextField()

    # is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email