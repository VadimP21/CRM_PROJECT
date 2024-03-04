"""Точки входа для приложения lead"""

from django.urls import path

from apps.lead.views import (
    LeadDeleteView,
    LeadCreateView,
    LeadUpdateView,
    LeadListView,
    LeadReadView,
)

app_name = "lead"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead_list"),
    path("create/", LeadCreateView.as_view(), name="lead_create"),
    path("<slug:pk>/", LeadReadView.as_view(), name="lead_read"),
    path(
        "<slug:pk>/update/",
        LeadUpdateView.as_view(),
        name="lead_update",
    ),
    path(
        "<slug:pk>/archive/",
        LeadDeleteView.as_view(),
        name="lead_delete",
    ),
]
