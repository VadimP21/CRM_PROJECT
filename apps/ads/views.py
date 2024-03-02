"""Модуль контроллер для приложения ads"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
    queryset = Advertisement.objects.select_related("product")
    context_object_name = "advertisement"

    def check_permission(self, codename):
        if self.request.user.is_superuser:
            return True
        return any(
            permission.codename == codename
            for permission in self.request.user.permissions
        )


class AdvertisementCreateView(AdvertisementView, CreateView):
    form_class = AdvertisementForm
    template_name = "ads/advertisement_create.html"

    def get_success_url(self):
        return reverse(
            "advertisement:advertisement_read",
            kwargs={"pk": self.object.pk},
        )


class AdvertisementReadView(AdvertisementView, DetailView):
    template_name_suffix = "_read"

    def test_func(self):
        return self.check_permission("add_advertisement")


class AdvertisementUpdateView(AdvertisementView, UpdateView):
    success_url = reverse_lazy("advertisement:advertisement_read")
    template_name_suffix = "_update"
    form_class = AdvertisementForm

    def get_success_url(self):
        return reverse(
            "advertisement:advertisement_read",
            kwargs={"pk": self.object.pk},
        )

    def test_func(self):
        return self.check_permission("add_advertisement")


class AdvertisementDeleteView(AdvertisementView, DeleteView):
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse(
            "advertisement:advertisement_list",
        )

    def test_func(self):
        return self.check_permission("add_advertisement")


class AdvertisementListView(AdvertisementView, ListView):
    queryset = Advertisement.objects.filter(is_active=True).only("name")
    context_object_name = "advertisements"

    def test_func(self):
        return self.check_permission("add_advertisement")


class AdvertisementStaticsView(AdvertisementView):
    #  TODO заполнить context
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "ads/advertisement_statistics.html",
            # {
            # ...
            # },
        )

    def test_func(self):
        return self.check_permission("add_advertisement")
