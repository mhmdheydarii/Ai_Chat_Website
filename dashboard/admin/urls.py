from django.urls import path, include
from . import views

app_name = "admin"

urlpatterns = [
    # Profile Urls
    path("profile/", views.AdminProfileview.as_view(), name="profile"),
    path("profile/edit/", views.AdminProfileEditView.as_view(), name="profile-edit"),
    path("change/password/", views.AdminChangePasswordView.as_view(), name="change-password"),

    # Management Urls
    path("management/", views.AdminManagementview.as_view(), name="management"),
    path("users/<int:pk>/detail/", views.AdminUsersDetailview.as_view(), name="users-detail"),
]
