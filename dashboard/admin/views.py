from django.shortcuts import redirect
from django.views.generic import View, TemplateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_view
from accounts.models import UserType, Profile, User
from dashboard.permissions import HasAdminPermission
from .forms import AdminProfileEditForm, AdminChangePasswordForm
from chat.models import ConversationModel
# Create your views here.

class AdminProfileview(LoginRequiredMixin, HasAdminPermission, TemplateView):
    template_name = "dashboard/admin/profile/profile.html"
    

class AdminProfileEditView(LoginRequiredMixin, HasAdminPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/profile/edit-profile.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = "اطلاعات شما بروزرسانی شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    

class AdminChangePasswordView(LoginRequiredMixin, HasAdminPermission, SuccessMessageMixin, auth_view.PasswordChangeView):
    template_name = "dashboard/admin/profile/change-password.html"
    form_class = AdminChangePasswordForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = "پسوورد شما بروزرسانی شد"


class AdminManagementview(LoginRequiredMixin, HasAdminPermission, ListView):
    queryset = User.objects.all()
    template_name = "dashboard/admin/management/user-management.html"
    context_object_name = "users"


class AdminUsersDetailview(LoginRequiredMixin, HasAdminPermission, DetailView):
    template_name = "dashboard/admin/management/user-detail.html"
    queryset = User.objects.all()
    context_object_name ="target_user"