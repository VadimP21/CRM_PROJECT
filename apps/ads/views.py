"""Модуль контроллер для приложения ads"""
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from apps.ads.forms import AdvertisementForm
from apps.ads.models import Advertisement


class AdvertisementView(View):
    model = Advertisement
    context_object_name = "ad"
    fields = (
        "name",
        "channel",
        "cost",
        "is_active",
        # "product",
    )


class AdvertisementCreateView(CreateView):
    queryset = Advertisement.objects.select_related("product")
    form_class = AdvertisementForm
    template_name = "ads/advertisement_create.html"
    success_url = reverse_lazy("advertisement:advertisement_read")

    def get_success_url(self):
        return reverse(
            "ads:ads_read",
            kwargs={"pk": self.object.pk},
        )


class AdvertisementReadView(DetailView, AdvertisementView):
    pass


class AdvertisementUpdateView(UpdateView, AdvertisementView):
    pass


class AdvertisementDeleteView(DeleteView, AdvertisementView):
    pass


class AdvertisementListView(ListView, AdvertisementView):
    queryset = Advertisement.objects.filter(is_active=True)
    context_object_name = "ads"


class AdvertisementStaticsView(View):
    pass
