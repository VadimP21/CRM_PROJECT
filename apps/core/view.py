"""Модуль контроллер для приложения core"""

from django.core.cache import cache
from django.shortcuts import render
from django.views import View

from apps.core.models import SiteSettings
from apps.product.models import Product
from config import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    def get_products_count(self, cache_time):
        products_count = cache.get(settings.PRODUCTS_SESSION_ID)
        if not products_count:
            products_count = Product.objects.filter(is_active=True).count
            cache.set(settings.PRODUCTS_SESSION_ID, products_count, cache_time)
        return products_count

    def get(self, request, *args, **kwargs):
        site_settings = SiteSettings.objects.get()
        products_count = self.get_products_count(site_settings.cache_time)

        context = {
            "products_count": products_count,
        }
        return render(request, "core/index.html", context)
