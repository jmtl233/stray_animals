from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import User, AdoptionApplication  # 添加导入
from pets.models import Pet

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard.html'    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取实际的待审核申请数量
        pending_adoptions = AdoptionApplication.objects.filter(status='pending').count()
        
        context.update({
            'show_stats': True,
            'stats': {
                'total_users': User.objects.count(),  # 真实用户数
                'pending_adoptions': pending_adoptions,  # 实际待审核数量
                'total_pets': Pet.objects.count()  # 真实宠物数
            },
            'user_management': False,  # 禁用未完成模块
            'pet_management': False    # 禁用宠物管理模块显示
        })
        return context


class AdminPetsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pet
    template_name = 'admin/pets.html'
    context_object_name = 'pets'
    paginate_by = 10  # 确保这里设置了分页数量
    
    def test_func(self):
        return self.request.user.is_staff
