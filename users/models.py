from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name='пароль')
    JWTToken = models.CharField(max_length=250, null=True, blank=True, verbose_name='JWT Token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
