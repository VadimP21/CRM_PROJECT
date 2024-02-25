"""Точки входа для приложения Accounts"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from .forms import LoginForm

app_name = "account"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            authentication_form=LoginForm,
            template_name="account/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="index.html",
            next_page=reverse_lazy("account:login"),
        ),
        name="logout",
    ),
]
