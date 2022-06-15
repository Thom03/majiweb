from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from .views import *

app_name = "accounts"

urlpatterns = [
    # path('register/', register, name='register'),
    # path('edit/', edit, name='edit'),
    path("dashboard/", dashboard, name="dashboard"),
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path("userlist/", userList, name="userlist"),
    # path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    # path('password_change/', PasswordChangeView.as_view(
    #     template_name='authapp/password_change_form.html'), name='password_change'),
    # path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
    #      name='password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(
    #     template_name='authapp/password_reset_form.html',
    #     email_template_name='authapp/password_reset_email.html',
    #     success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(
    #     template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='authapp/password_reset_confirm.html',
    #     success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(
    #     template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),
]
