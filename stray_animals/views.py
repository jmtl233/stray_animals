from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm  # 从具体应用导入
from users.models import User  # 从自定义用户模型导入
from pets.models import Pet
from announcements.models import Announcement
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def dashboard(request):
    return render(request, 'admin/dashboard.html', {
        'show_stats': True,
        'stats': {
            'total_users': User.objects.count(),  # 真实用户数量
            'pending_adoptions': 0,  # 待实现功能
            'total_pets': Pet.objects.count()  # 真实宠物数量
        }
    })

def user_management(request):
    from users.models import User
    user_list = User.objects.all()
    paginator = Paginator(user_list, 10)  # 每页10条
    
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {
        'user_management': True,
        'users': users,  # 传递分页对象
        'stats': {
            'total_users': User.objects.count(),
            'pending_adoptions': 0,
            'total_pets': Pet.objects.count()
        }
    })

def pet_management(request):
    pets = Pet.objects.all()
    return render(request, 'admin/dashboard.html', {
        'pet_management': True,  # 激活宠物管理模块
        'pets': pets,
        'stats': {  # 保持统计数据显示
            'total_users': User.objects.count(),
            'pending_adoptions': 0
        }
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

@login_required
def home_view(request):
    return render(request, 'home/home.html')

def success_cases_view(request):
    animal_type = request.GET.get('type', 'all')
    success_cases = Pet.objects.filter(is_adopted=True)
    
    if animal_type == 'cat':
        success_cases = success_cases.filter(breed__contains='猫')
    elif animal_type == 'dog':
        success_cases = success_cases.filter(breed__contains='犬')

    return render(request, 'home/success_cases.html', {
        'success_cases': success_cases,
        'current_type': animal_type
    }) 