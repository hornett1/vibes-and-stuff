from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', default='users/user_default.png')
    banner = models.ImageField(upload_to='users/', default='users/user_default.png')
    about = models.CharField(max_length=210,blank=True)

    def __str__(self):
        return self.username