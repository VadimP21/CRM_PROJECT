"""Модуль контроллер для приложения contract"""

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

from apps.contract.forms import ContractForm
from apps.contract.models import Contract


class ContractView(View):
    queryset = Contract.objects.select_related("product")
    context_object_name = "contract"

    def check_permission(self, codename):
        if self.request.user.is_superuser:
            return True
        return any(
            permission.codename == codename
            for permission in self.request.user.permissions
        )


class ContractCreateView(ContractView, CreateView):
    form_class = ContractForm
    template_name = "contract/contract_create.html"


class ContractReadView(ContractView, DeleteView):
    template_name_suffix = "_read"


class ContractUpdateView(ContractView, UpdateView):
    success_url = reverse_lazy("contract:contract_read")
    template_name_suffix = "_update"
    form_class = ContractForm

    def get_success_url(self):
        return reverse(
            "contract:contract_read",
            kwargs={"pk": self.object.pk},
        )


class ContractDeleteView(ContractView, DetailView):
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse(
            "contract:contract_list",
        )


class ContractListView(ContractView, ListView):
    queryset = Contract.objects.fiter(arcived=False).only("name")
    context_object_name = "contracts"
