from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(blank=False, null=False, max_length=150)
    last_name = models.CharField(blank=False, null=False, max_length=150)
