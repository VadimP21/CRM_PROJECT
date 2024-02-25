"""Точки входа для приложения Core"""

from django.urls import path

from apps.core.view import IndexView

app_name = "core"

urlpatterns = [
    path(
        "index/",
        IndexView.as_view(),
        name="index",
    ),
]
