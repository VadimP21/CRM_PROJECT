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

from apps.lead.forms import LeadForm
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


class LeadCreateView(LeadView, CreateView):
    form_class = LeadForm
    template_name = "lead/lead_create.html"

    def get_success_url(self):
        return reverse(
            "lead:lead_read",
            kwargs={"pk": self.object.pk},
        )


class LeadReadView(LeadView, DetailView):
    template_name_suffix = "_read"


class LeadUpdateView(LeadView, UpdateView):
    success_url = reverse_lazy("lead:lead_read")
    template_name_suffix = "_update"
    form_class = LeadForm

    def get_success_url(self):
        return reverse(
            "lead:lead_read",
            kwargs={"pk": self.object.pk},
        )


class LeadDeleteView(LeadView, DeleteView):
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse(
            "lead:lead_list",
        )


class LeadListView(LeadView, ListView):
    queryset = Lead.objects.filter(archived=False).only("last_name", "first_name")

    context_object_name = "leads"
