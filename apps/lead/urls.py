"""Точки входа для приложения lead"""

from django.urls import path

from apps.lead.views import (
    LeadDeleteView,
    LeadStaticsView,
    LeadCreateView,
    LeadUpdateView,
    LeadListView,
    LeadReadView,
)

app_name = "lead"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead_list"),
    path(
        "statistics",
        LeadStaticsView.as_view(),
        name="Lead_statistics",
    ),
    path("create/", LeadCreateView.as_view(), name="Lead_create"),
    path("<slug:pk>/", LeadReadView.as_view(), name="Lead_read"),
    path(
        "<slug:pk>/update/",
        LeadUpdateView.as_view(),
        name="Lead_update",
    ),
    path(
        "<slug:pk>/archive/",
        LeadDeleteView.as_view(),
        name="Lead_delete",
    ),
]
