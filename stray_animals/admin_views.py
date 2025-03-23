from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import User
from pets.models import Pet

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'show_stats': True,
            'stats': {
                'total_users': User.objects.count(),  # 真实用户数
                'pending_adoptions': 0,  # 待实现功能
                'total_pets': Pet.objects.count()  # 真实宠物数
            },
            'user_management': False,  # 禁用未完成模块
            'pet_management': False    # 禁用宠物管理模块显示
        })
        return context 