"""Модуль контроллер для приложения core"""

from django.core.cache import cache
from django.shortcuts import render
from django.views import View

from apps.core.models import SiteSettings
from apps.lead.models import Lead
from apps.product.models import Product
from apps.ads.models import Advertisement
from django.contrib.auth.mixins import LoginRequiredMixin

from config.settings import (
    PRODUCTS_SESSION_ID,
    ADVERTISEMENT_SESSION_ID,
    LEAD_SESSION_ID,
)


class IndexView(LoginRequiredMixin, View):
    def get_products_count(self, cache_time):
        products_count = cache.get(PRODUCTS_SESSION_ID)
        if not products_count:
            products_count = Product.objects.filter(is_active=True).count
            cache.set(PRODUCTS_SESSION_ID, products_count, cache_time)
        return products_count

    def get_advertisements_count(self, cache_time):
        products_count = cache.get(ADVERTISEMENT_SESSION_ID)
        if not products_count:
            products_count = Advertisement.objects.filter(is_active=True).count
            cache.set(ADVERTISEMENT_SESSION_ID, products_count, cache_time)
        return products_count

    def get_leads_count(self, cache_time):
        products_count = cache.get(LEAD_SESSION_ID)
        if not products_count:
            products_count = Lead.objects.count
            cache.set(LEAD_SESSION_ID, products_count, cache_time)
        return products_count

    def get(self, request, *args, **kwargs):
        site_settings = SiteSettings.objects.get()
        products_count = self.get_products_count(site_settings.cache_time)
        advertisements_count = self.get_advertisements_count(site_settings.cache_time)
        leads_count = self.get_leads_count(site_settings.cache_time)

        context = {
            "products_count": products_count,
            "advertisements_count": advertisements_count,
            "leads_count": leads_count,
        }
        return render(request, "core/index.html", context)
