from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from django.contrib import messages

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'login/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_superuser:
            messages.success(self.request, 'admin 管理员身份验证成功')
        return response

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'login/register.html'
    success_url = '/login/'

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return super().form_invalid(form)

class LogoutView(AuthLogoutView):
    next_page = '/login/' 