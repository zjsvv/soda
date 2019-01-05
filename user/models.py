from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # add additional fields in here
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.email
