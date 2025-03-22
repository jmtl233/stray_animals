from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
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
