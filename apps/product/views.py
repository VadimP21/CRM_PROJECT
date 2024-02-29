"""Модуль контроллер для приложения products"""

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from apps.product.models import Product
from django.contrib.auth.mixins import UserPassesTestMixin


class ProductView(View):
    model = Product

    context_object_name = "product"
    fields = (
        "name",
        "price",
        "description",
        "is_active",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perms"] = list(
            permission.codename for permission in self.request.user.permissions
        )
        return context

    def check_permission(self, codename):
        if self.request.user.is_superuser:
            return True
        return any(
            permission.codename == codename
            for permission in self.request.user.permissions
        )


class ProductCreateView(UserPassesTestMixin, ProductView, CreateView):
    template_name_suffix = "_create"
    success_url = reverse_lazy("product:product_read")

    def get_success_url(self):
        return reverse(
            "product:product_read",
            kwargs={"pk": self.object.pk},
        )

    def test_func(self):
        return self.check_permission("add_product")


class ProductReadView(UserPassesTestMixin, ProductView, DetailView):
    def test_func(self):
        return self.check_permission("view_product")


class ProductUpdateView(UserPassesTestMixin, ProductView, UpdateView):
    success_url = reverse_lazy("product:product_read")
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse(
            "product:product_read",
            kwargs={"pk": self.object.pk},
        )

    def test_func(self):
        return self.check_permission("change_product")


class ProductDeleteView(UserPassesTestMixin, ProductView, DeleteView):

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse(
            "product:products_list",
        )

    def test_func(self):
        return self.check_permission("delete_product")


class ProductListView(UserPassesTestMixin, ProductView, ListView):
    queryset = Product.objects.filter(is_active=True)
    context_object_name = "products"

    def test_func(self):
        return self.check_permission("view_product")
