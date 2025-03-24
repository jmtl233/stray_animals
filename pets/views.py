from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pet  # 需要先创建Pet模型

# Create your views here.

def test_view(request):
    return HttpResponse("Pets app works!")

class PetListView(ListView):
    model = Pet
    template_name = 'pets/list.html'
    context_object_name = 'pets'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
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

class PetCreateView(CreateView):
    model = Pet
    fields = ['name', 'breed', 'age', 'gender', 'photo', 'is_vaccinated', 'is_neutered', 'health_status', 'description']
    template_name = 'pets/create.html'
    success_url = '/pets/list/'

    def form_valid(self, form):
        # 自动设置上传者（如果需要）
        # form.instance.uploader = self.request.user
        return super().form_valid(form)

class PetUpdateView(UpdateView):
    model = Pet
    fields = ['name', 'breed', 'age', 'gender', 'photo', 'is_vaccinated', 'is_neutered', 'health_status', 'description']
    template_name = 'pets/create.html'  # 可以复用创建模板
    success_url = '/admin/pets/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_mode'] = True  # 添加编辑模式标识
        return context

class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy('admin_pets')  # 删除后跳转到宠物管理页
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
