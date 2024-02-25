"""Модуль контроллер для приложения products"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from apps.product.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "price", "description", "is_active",
    success_url = reverse_lazy("products:product_read")


class ProductReadView(DetailView):
    model = Product
    fields = "name", "price", "description", "is_active",


class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "price", "description", "is_active",
    success_url = reverse_lazy("products:product_read")
    # template_name_suffix = "_update_form"


class ProductDeleteView(DeleteView):
    model = Product

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductListView(ListView):
    context_object_name = "products"
    queryset = Product.objects.filter(is_active=True)