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
from django.views.generic import RedirectView, TemplateView
from . import admin_views, views  # 需要创建admin_views.py和确保导入视图模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('users:login')), name='root_redirect'),
    path('login/', RedirectView.as_view(url=reverse_lazy('users:login')), name='login_redirect'),
    path('admin/dashboard/', admin_views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/users/', views.user_management, name='admin_users'),
    path('admin/pets/', views.pet_management, name='admin_pets'),
    path('admin/announcements/', views.announcement_management, name='admin_announcements'),
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('home/', views.home_view, name='home'),
    path('pets/', include('pets.urls', namespace='pets')),
    path('events/', include('events.urls', namespace='events')),
    path('announcements/', include('announcements.urls', namespace='announcements')),
    path('admin/adoptions/', views.adoption_management, name='admin_adoptions'),
    path('success-cases/', views.success_cases_view, name='success_cases'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
