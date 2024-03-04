"""Точки входа для приложения ads"""

from django.urls import path

from apps.ads.views import (
    AdvertisementDeleteView,
    AdvertisementStaticsView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementListView,
    AdvertisementReadView,
)

app_name = "advertisement"

urlpatterns = [
    path("", AdvertisementListView.as_view(), name="advertisement_list"),
    path(
        "statistics",
        AdvertisementStaticsView.as_view(),
        name="advertisement_statistics",
    ),
    path("create/", AdvertisementCreateView.as_view(), name="advertisement_create"),
    path("<slug:pk>/", AdvertisementReadView.as_view(), name="advertisement_read"),
    path(
        "<slug:pk>/update/",
        AdvertisementUpdateView.as_view(),
        name="advertisement_update",
    ),
    path(
        "<slug:pk>/archive/",
        AdvertisementDeleteView.as_view(),
        name="advertisement_delete",
    ),
]
