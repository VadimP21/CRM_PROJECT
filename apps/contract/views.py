"""Модуль контроллер для приложения ads"""

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


class ContractView(View):
    pass


class ContractCreateView(ContractView, CreateView):
    pass


class ContractReadView(ContractView, DeleteView):
    pass


class ContractUpdateView(ContractView, UpdateView):
    pass


class ContractDeleteView(ContractView, DeleteView):
    pass


class ContractListView(ContractView, ListView):
    pass
