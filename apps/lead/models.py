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
)

from apps.ads.models import Advertisement


class Lead(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=100, verbose_name="Фамилия")
    last_name = CharField(max_length=100, verbose_name="Имя")
    phone = CharField(
        max_length=18,
        unique=True,
        verbose_name="Телефон",
        validators=[
            RegexValidator(
                r"^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$",
                message=("Номер телефона должен быть в формате +7 (999) 999-99-99"),
            )
        ],
    )
    email = EmailField(unique=True, verbose_name="Email")
    advertisement = ForeignKey(
        Advertisement, verbose_name="Рекламная кампания", on_delete=DO_NOTHING
    )
