from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm  # 从具体应用导入
from users.models import User  # 从自定义用户模型导入

def dashboard(request):
    return render(request, 'admin/dashboard.html', {'show_stats': True})

def user_management(request):
    users = User.objects.all()  # 需要导入User模型
    return render(request, 'admin/dashboard.html', {
        'user_management': True,
        'users': users  # 传递用户数据
    })

def adoption_management(request):
    # 领养审核逻辑
    return render(request, 'admin/dashboard.html', {'adoption_management': True}) 