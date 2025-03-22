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
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from . import admin_views, views  # 需要创建admin_views.py和确保导入视图模块

urlpatterns = [
    path('admin/dashboard/', views.dashboard, name='admin_dashboard'),
    path('admin/users/', views.user_management, name='admin_users'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', RedirectView.as_view(url='/users/'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='home/home.html'), name='dashboard'),
    path('pets/', include('pets.urls', namespace='pets')),  # 取消注释
    path('events/', include('events.urls', namespace='events')),
    path('announcements/', include('announcements.urls', namespace='announcements')),
    path('admin/announcements/', include('announcements.urls', namespace='admin_announcements')),
    path('admin/adoptions/', views.adoption_management, name='admin_adoptions'),
]
