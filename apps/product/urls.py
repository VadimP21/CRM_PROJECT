"""Точки входа для приложения Products"""

from django.urls import path

from apps.product.views import ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, ProductReadView

app_name = "product"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductReadView.as_view(), name="product_read"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
]

