"""Точки входа для приложения Products"""

from django.urls import path

from apps.product.views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
    ProductReadView,
)

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<slug:pk>/", ProductReadView.as_view(), name="product_read"),
    path("<slug:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<slug:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
]
