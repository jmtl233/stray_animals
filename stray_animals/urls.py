"""stray_animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings  # 新增导入
from django.conf.urls.static import static  # 新增导入
from . import admin_views, views
from adoptions import views as adoptions_views

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('users:login')), name='root_redirect'),
    path('login/', RedirectView.as_view(url=reverse_lazy('users:login')), name='login_redirect'),
    
    # 将自定义管理路由放在 admin.site.urls 之前
    path('admin/dashboard/', admin_views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/users/', views.user_management, name='admin_users'),
    path('admin/pets/', views.pet_management, name='admin_pets'),
    path('admin/announcements/', views.announcement_management, name='admin_announcements'),
    # 领养管理路由组
    path('admin/adoptions/', include([
        path('', views.adoption_management, name='admin_adoptions'),
        path('<int:pk>/', adoptions_views.AdoptionDetailView.as_view(), name='admin_adoption_detail'),
        # 添加审批和拒绝的路由
        path('approve/<int:application_id>/', adoptions_views.approve_application, name='approve_application'),
        path('reject/<int:application_id>/', adoptions_views.reject_application, name='reject_application'),
    ])),
    
    # Django 原生 admin 路由放在最后
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('home/', views.home_view, name='home'),
    path('pets/', include('pets.urls', namespace='pets')),
    path('events/', include('events.urls', namespace='events')),
    path('announcements/', include('announcements.urls', namespace='announcements')),
    # 删除重复的路由
    # path('admin/adoptions/', views.adoption_management, name='admin_adoptions'),
    path('success-cases/', views.success_cases_view, name='success_cases'),
    
    # 添加领养申请路由
    path('apply/<int:pet_id>/', adoptions_views.apply_adoption, name='apply_adoption'),
    # 删除重复的路由，已经在上面的include中添加了
    # path('admin/adoptions/reject/<int:application_id>/', adoptions_views.reject_application, name='reject_application'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
