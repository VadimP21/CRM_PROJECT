"""Точки входа для приложения ads"""

from django.urls import path

from apps.core.view import IndexView

app_name = "ads"

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
]
