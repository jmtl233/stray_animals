from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'show_stats': True,
            'stats': {
                'total_users': 100,  # 临时测试数据
                'pending_adoptions': 5, 
                'total_pets': 50
            },
            'user_management': False,  # 禁用未完成模块
            'pet_management': True    # 启用已实现的宠物管理
        })
        return context 