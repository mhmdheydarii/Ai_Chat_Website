from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_view
from django.shortcuts import get_object_or_404
from accounts.models import UserType, Profile, User
from dashboard.permissions import HasAdminPermission
from .forms import AdminProfileEditForm, AdminChangePasswordForm
from chat.models import ConversationModel, MessageModel
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


class AdminUsersListview(LoginRequiredMixin, HasAdminPermission, ListView):
    
    template_name = "dashboard/admin/management/user-list.html"

    def get_queryset(self):
        queryset = User.objects.all()

        if search_q:= self.request.GET.get("q"):
            queryset = queryset.filter(username=search_q)
        return queryset  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = self.get_queryset()
        context["status_types"] = UserType.choices
        return context


class AdminUsersDetailview(LoginRequiredMixin, HasAdminPermission, DetailView):
    template_name = "dashboard/admin/management/user-detail.html"
    queryset = User.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.get_object()
        context["user"] = User.objects.get(username=username)
        context["conversations"] = ConversationModel.objects.all().filter(user=username)
        return context
    

class AdminActivateUserView(LoginRequiredMixin, HasAdminPermission, View):

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get("pk"))

        user.is_active = True
        user.save()
        return redirect(reverse_lazy("dashboard:admin:users-list"))


class AdminDeactivateUserView(LoginRequiredMixin, HasAdminPermission, View):

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get("pk"))

        user.is_active = False
        user.save()
        return redirect(reverse_lazy("dashboard:admin:users-list"))
    

class AdminConversationDetailView(LoginRequiredMixin, HasAdminPermission, View):

    def get(self, request, user_pk, conv_pk):
        
        user = get_object_or_404(User, pk=user_pk)
        conversation = get_object_or_404(ConversationModel, pk=conv_pk, user__id=user_pk)

        return render(request, 'dashboard/admin/management/conversation-detail.html',
                        {"conversation":conversation, "user":user})

