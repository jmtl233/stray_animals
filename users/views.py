from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import CreateView, DetailView, DeleteView, TemplateView
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import User, AdoptionApplication
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # 获取用户的领养申请记录
        context['pending_applications'] = AdoptionApplication.objects.filter(
            user=user,
            status='pending'
        ).select_related('pet')
        
        context['approved_applications'] = AdoptionApplication.objects.filter(
            user=user,
            status='approved'
        ).select_related('pet')
        
        context['rejected_applications'] = AdoptionApplication.objects.filter(
            user=user,
            status='rejected'
        ).select_related('pet')
        
        return context


@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        
        # 更新用户名、邮箱和手机号
        username = request.POST.get('username', '')
        if username and username != user.username:
            # 检查用户名是否已存在
            if User.objects.filter(username=username).exists():
                messages.error(request, '用户名已被使用')
            else:
                user.username = username
        
        user.email = request.POST.get('email', '')
        user.phone = request.POST.get('phone', '')
        
        # 处理头像上传
        if 'avatar' in request.FILES:
            user.avatar = request.FILES['avatar']
        
        user.save()
        messages.success(request, '个人资料已更新')
        return redirect('users:profile')
    
    return redirect('users:profile')