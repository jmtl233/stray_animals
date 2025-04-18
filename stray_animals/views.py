from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm  # 从具体应用导入
from users.models import User  # 从自定义用户模型导入
from pets.models import Pet
from announcements.models import Announcement
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q  # 添加这行导入

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
    
    # 获取搜索查询参数
    search_query = request.GET.get('q', '')
    
    # 基础查询集
    user_list = User.objects.all()
    
    # 如果有搜索查询，过滤用户列表
    if search_query:
        user_list = user_list.filter(
            Q(username__icontains=search_query) |  # 用户名包含搜索词
            Q(email__icontains=search_query) |     # 邮箱包含搜索词
            Q(phone__icontains=search_query)       # 手机号包含搜索词
        )
    
    paginator = Paginator(user_list, 10)  # 每页10条
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {
        'user_management': True,
        'users': users,
        'search_query': search_query,  # 传递搜索查询到模板
        'stats': {
            'total_users': User.objects.count(),
            'pending_adoptions': 0,
            'total_pets': Pet.objects.count()
        }
    })

def pet_management(request):
    # 获取搜索查询参数和状态筛选
    search_query = request.GET.get('q', '')
    status_filter = request.GET.get('status', 'all')
    
    # 基础查询集
    pets = Pet.objects.all()
    
    # 应用状态筛选
    if status_filter and status_filter != 'all':
        pets = pets.filter(status=status_filter)
    
    # 应用搜索过滤
    if search_query:
        pets = pets.filter(
            Q(name__icontains=search_query) | 
            Q(breed__icontains=search_query)
        )
    
    # 分页处理
    paginator = Paginator(pets, 10)
    page_number = request.GET.get('page')
    pets = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {
        'pet_management': True,
        'pets': pets,
        'search_query': search_query,
        'status_filter': status_filter,  # 传递当前筛选状态到模板
        'stats': {
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
    print(f"当前用户认证状态: {request.user.is_authenticated}")  # 调试输出
    print(f"用户对象: {request.user}")  # 调试输出
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