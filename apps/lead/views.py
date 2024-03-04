from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from apps.lead.models import Lead


class LeadView(View):
    queryset = Lead.objects.select_related("advertisement")
    context_object_name = "lead"

    def check_permission(self, codename):
        if self.request.user.is_superuser:
            return True
        return any(
            permission.codename == codename
            for permission in self.request.user.permissions
        )


class LeadCreateView:
    pass


class LeadReadView:
    pass


class LeadUpdateView:
    pass


class LeadDeleteView:
    pass


class LeadListView:
    pass
