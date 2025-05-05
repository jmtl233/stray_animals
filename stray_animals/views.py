from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserForm  # 从具体应用导入
from users.models import User  # 从自定义用户模型导入
from pets.models import Pet
from announcements.models import Announcement
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q  # 添加这行导入
from users.models import User, AdoptionApplication  # 确保包含AdoptionApplication导入

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
    # 获取搜索查询参数
    search_query = request.GET.get('q', '')
    
    # 基础查询集
    announcements = Announcement.objects.all().order_by('-publish_date')
    
    # 如果有搜索查询，过滤公告列表
    if search_query:
        announcements = announcements.filter(title__icontains=search_query)
    
    # 分页处理
    paginator = Paginator(announcements, 10)  # 每页10条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {
        'announcement_management': True,
        'announcements': page_obj,
        'page_obj': page_obj,
        'search_query': search_query
    })

def adoption_management(request):
    status_filter = request.GET.get('status', 'all')
    search_query = request.GET.get('q', '')
    
    applications = AdoptionApplication.objects.select_related('user', 'pet').order_by('-apply_date')
    
    if status_filter != 'all':
        applications = applications.filter(status=status_filter)
        
    if search_query:
        applications = applications.filter(
            Q(user__username__icontains=search_query) |
            Q(pet__name__icontains=search_query)
        )
    
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {  # 修改为渲染dashboard.html
        'adoption_management': True,
        'applications': applications,
        'status_filter': status_filter,
        'search_query': search_query
    })

@login_required
def home_view(request):
    print(f"当前用户认证状态: {request.user.is_authenticated}")  # 调试输出
    print(f"用户对象: {request.user}")  # 调试输出
    return render(request, 'home/home.html')

def success_cases(request):
    """成功救助案例页面"""
    # 获取类型过滤参数
    pet_type = request.GET.get('type', '')
    
    # 查询已有救助故事的宠物
    query = Pet.objects.filter(rescue_story__isnull=False, rescue_story__gt='')
    
    # 根据类型过滤
    if pet_type == 'cat':
        query = query.filter(breed__in=['中华田园猫', '布偶猫', '英国短毛猫', '波斯猫', '暹罗猫'])
    elif pet_type == 'dog':
        query = query.filter(breed__in=['中华田园犬', '金毛寻回犬', '拉布拉多', '哈士奇', '柯基犬'])
    
    # 确保rescue_date字段有值
    success_cases = query.exclude(rescue_date__isnull=True).order_by('-rescue_date')
    
    # 如果没有找到有救助日期的案例，则使用所有有救助故事的宠物
    if not success_cases.exists():
        success_cases = query.order_by('-id')
    
    return render(request, 'home/success_cases.html', {
        'success_cases': success_cases
    })

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

# 在文件顶部添加必要的导入
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# 在文件中添加以下视图函数
@require_POST
def clear_announcement(request):
    """清除会话中的公告信息"""
    if 'announcement_id' in request.session:
        del request.session['announcement_id']
    if 'announcement_title' in request.session:
        del request.session['announcement_title']
    if 'announcement_content' in request.session:
        del request.session['announcement_content']
    return JsonResponse({'status': 'success'})

# 在文件中添加以下函数
# 添加以下导入（如果尚未导入）
from django.shortcuts import render
from django.core.paginator import Paginator

# 添加event_management视图函数
def event_management(request):
    from events.models import Event
    from django.core.paginator import Paginator
    
    search_query = request.GET.get('q', '')
    
    events = Event.objects.all().order_by('-created_at')
    
    if search_query:
        events = events.filter(title__icontains=search_query)
    
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)
    
    return render(request, 'admin/dashboard.html', {
        'event_management': True,
        'events': events,
        'search_query': search_query
    })

    