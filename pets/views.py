from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Pet  # 需要先创建Pet模型

# Create your views here.

def test_view(request):
    return HttpResponse("Pets app works!")

class PetListView(ListView):
    model = Pet
    template_name = 'pets/list.html'
    context_object_name = 'pets'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/detail.html'
    context_object_name = 'pet'

class PetCreateView(CreateView):
    model = Pet
    fields = '__all__'  # 实际开发时应指定具体字段
    template_name = 'pets/create.html'
    success_url = '/pets/list/'
