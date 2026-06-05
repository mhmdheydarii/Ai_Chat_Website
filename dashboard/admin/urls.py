from django.urls import path, include
from . import views

app_name = "admin"

urlpatterns = [
    # Profile Urls
    path("profile/", views.AdminProfileview.as_view(), name="profile"),
    path("profile/edit/", views.AdminProfileEditView.as_view(), name="profile-edit"),
    path("change/password/", views.AdminChangePasswordView.as_view(), name="change-password"),

    # Management Urls
    path("users/list/", views.AdminUsersListview.as_view(), name="users-list"),
    path("users/<int:pk>/detail/", views.AdminUsersDetailview.as_view(), name="users-detail"),
    path("conversation/<int:conv_pk>/user/<int:user_pk>/", views.AdminConversationDetailView.as_view(), name="conversation-detail"),
    
    path("user/<int:pk>/activate/", views.AdminActivateUserView.as_view(), name="user-activate"),
    path("user/<int:pk>/deactivate/", views.AdminDeactivateUserView.as_view(), name="user-deactivate"),


]
