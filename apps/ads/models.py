"""Модуль с моделями приложения ads"""

from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DO_NOTHING,
    DecimalField,
    BooleanField,
)

from apps.product.models import Product


class Advertisement(Model):
    name = CharField(primary_key=True, max_length=128, verbose_name="Название")
    product = ForeignKey(Product, verbose_name="Услуга", on_delete=DO_NOTHING)
    channel = CharField(max_length=255, verbose_name="Канал продвижения")
    cost = DecimalField(max_digits=16, decimal_places=2, verbose_name="Бюджет")
    is_active = BooleanField(default=1, verbose_name="Активен")

    def __str__(self):
        return f"Advertisement {self.name!r}"
