from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

    # List of all the other Users, the logged-in user is following
    is_following = models.ManyToManyField(to="self", related_name='is_followed_by', blank=True, default=None, symmetrical=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)