from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from pets.models import Pet
from users.models import AdoptionApplication

class AdoptionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = AdoptionApplication
    template_name = 'admin/adoption_detail.html'
    
    def test_func(self):
        return self.request.user.is_staff
class AdoptionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AdoptionApplication
    fields = ['status', 'notes']
    template_name = 'admin/adoption_review.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        form.instance.reviewed_by = self.request.user
        return super().form_valid(form)


def apply_adoption(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        # 创建领养申请记录
        AdoptionApplication.objects.create(
            user=request.user,
            pet=pet,
            status='pending',
            contact_info=request.user.phone,  # 需要根据实际情况获取联系方式
            experience=""  # 需要添加表单字段来收集这些信息
        )
        messages.success(request, '领养申请已提交！')
        return redirect('pets:detail', pet.id)
    return redirect('pets:list')
