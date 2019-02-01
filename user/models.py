from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # overwritten field
    email = models.EmailField(_('email address'), unique=True)

    # add additional fields in here
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.email
