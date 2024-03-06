"""Модуль с моделями приложения lead"""

import uuid

from django.core.validators import RegexValidator
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DO_NOTHING,
    UUIDField,
    EmailField,
    BooleanField,
)

from apps.ads.models import Advertisement


class Lead(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=100, verbose_name="Фамилия")
    last_name = CharField(max_length=100, verbose_name="Имя")
    phone = CharField(
        max_length=12,
        unique=True,
        verbose_name="Телефон",
    )
    email = EmailField(unique=True, verbose_name="Email")
    advertisement = ForeignKey(
        Advertisement, verbose_name="Рекламная кампания", on_delete=DO_NOTHING
    )
    is_active = BooleanField(default=0, verbose_name="Активен")
    archived = BooleanField(default=0, verbose_name="В архиве")

    def __str__(self):
        return f"Lead {self.first_name!r} {self.last_name!r}"
