from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm  # 从具体应用导入
from users.models import User  # 从自定义用户模型导入
from pets.models import Pet
from announcements.models import Announcement

def dashboard(request):
    return render(request, 'admin/dashboard.html', {
        'show_stats': True  # 仅显示统计模块
    })

def user_management(request):
    users = User.objects.all()
    return render(request, 'admin/dashboard.html', {
        'user_management': True,  # 激活用户管理模块
        'users': users
    })

def pet_management(request):
    pets = Pet.objects.all()
    return render(request, 'admin/dashboard.html', {
        'pet_management': True,  # 激活宠物管理模块
        'pets': pets
    })

def announcement_management(request):
    announcements = Announcement.objects.all()
    return render(request, 'admin/dashboard.html', {
        'announcement_management': True,  # 激活公告管理模块
        'announcements': announcements
    })

def adoption_management(request):
    # 领养审核逻辑
    return render(request, 'admin/dashboard.html', {'adoption_management': True}) 