"""Модуль для админ панели приложения products"""
from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price", "description")
    ordering = (
        "pk", "name", "price", "description"
    )
    search_fields = "name", "price"
