from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import CreateView, DetailView, DeleteView
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import User

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'login/login.html'

    def get_success_url(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return reverse('admin_dashboard')  # 管理员跳转后台
        return reverse('home')  # 普通用户跳转首页

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('users:login')

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return super().form_invalid(form)

class LogoutView(AuthLogoutView):
    next_page = 'users:login'  # 使用带命名空间的URL名称 

class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = get_user_model()
    template_name = 'admin/user_detail.html'
    context_object_name = 'target_user'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_management'] = True
        return context

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_users')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        return context