from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # 添加这一行
from .models import Pet  # 需要先创建Pet模型
from .forms import PetForm

# Create your views here.

def test_view(request):
    return HttpResponse("Pets app works!")

class PetListView(ListView):
    model = Pet
    template_name = 'pets/list.html'
    context_object_name = 'pets'
    paginate_by = 12  # 确保设置了分页数量

    def get_queryset(self):
        queryset = super().get_queryset().filter(status='available')
        breed_filter = self.request.GET.get('breed', '')
        if breed_filter:
            queryset = queryset.filter(breed=breed_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取所有品种选项（去重）
        context['breeds'] = dict(Pet.BREED_CHOICES).keys()
        return context

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/detail.html'
    context_object_name = 'pet'

class PetCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/create.html'
    # 修改成功后的跳转地址为管理后台的宠物列表页面
    success_url = reverse_lazy('admin_pets')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_mode'] = False
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class PetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # 添加安全混入类
    model = Pet
    form_class = PetForm  # 使用与创建视图相同的表单类
    template_name = 'pets/create.html'  # 可以复用创建模板
    success_url = reverse_lazy('admin_pets')  # 使用 reverse_lazy 保持一致性
    
    def test_func(self):  # 添加权限检查
        return self.request.user.is_staff
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_mode'] = True  # 添加编辑模式标识
        return context

class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy('admin_pets')  # 删除后跳转到宠物管理页
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

def create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_pets')
    else:
        form = PetForm()  # 确保正确初始化表单
    
    return render(request, 'pets/create.html', {
        'form': form,
        'edit_mode': False
    })
