from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя
    """
    username = models.CharField(max_length = 40, unique = True)
    email = models.EmailField(unique = True, blank = False, null = False)
    is_support = models.BooleanField(default=False, )
