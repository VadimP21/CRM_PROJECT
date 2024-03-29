"""Модуль с моделями приложения account"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель Пользователь c авторизацией через email"""

    class Meta:
        db_table = "auth_user"

    username = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        unique=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    @property
    def role(self):
        if hasattr(self, "profile") and self.profile.role:
            return self.profile.role.name

    @property
    def permissions(self):
        if hasattr(self, "profile") and self.profile.role:
            return self.profile.role.permissions.all()
        return []


class Role(models.Model):
    """Модель Роль для определения роли пользователя в системе"""

    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return f"{self.name}"


class Profile(models.Model):
    """Модель Профиля пользователя для связи Роли и Пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Profile(user={self.user} )"
