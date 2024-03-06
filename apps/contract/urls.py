"""Точки входа для приложения contract"""

from django.urls import path

from apps.contract.views import (
    ContractDeleteView,
    ContractCreateView,
    ContractUpdateView,
    ContractListView,
    ContractReadView,
)

app_name = "contract"

urlpatterns = [
    path("", ContractListView.as_view(), name="contract_list"),
    path("create/", ContractCreateView.as_view(), name="contract_create"),
    path("<slug:pk>/", ContractReadView.as_view(), name="contract_read"),
    path(
        "<slug:pk>/update/",
        ContractUpdateView.as_view(),
        name="contract_update",
    ),
    path(
        "<slug:pk>/archive/",
        ContractDeleteView.as_view(),
        name="contract_delete",
    ),
]
