"""Модуль с моделями приложения contract"""

import os

from django.core.exceptions import ValidationError
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DO_NOTHING,
    DecimalField,
    BooleanField,
    FileField,
    DateField,
)

from apps.product.models import Product


def validate_file(field_file_obj):
    file_size = field_file_obj.file.size
    if file_size > 5 * 1024 * 1024:
        raise ValidationError("Максимальный вес файла 5 MB")


def get_contract_file_path(instance: "Contract", filename: str) -> str:
    ext = os.path.splitext(filename)[1]
    return "files/{0}{1}".format(instance.name, ext)


class Contract(Model):
    name = CharField(max_length=128, verbose_name="Название")
    product = ForeignKey(Product, verbose_name="Услуга", on_delete=DO_NOTHING)
    file = FileField(
        upload_to=get_contract_file_path,
        validators=[validate_file],
        verbose_name="Файл",
    )
    start_date = DateField(verbose_name="Дата заключения")
    end_date = DateField(verbose_name="Дата окончания")
    cost = DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма")
    archived = BooleanField(default=0, verbose_name="В архиве")

    def __str__(self):
        return f"Contract {self.name!r}"
