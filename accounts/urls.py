from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisteView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout"),

    # password reset urls
    path("password/reset/", views.CustomPasswordResetView.as_view(), name="password-reset"),
    path("password/reset/sent/", views.CustomPasswordResetDoneView.as_view(), name="password-reset-sent"),
    path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
