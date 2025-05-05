from django.urls import path
from . import views

app_name = 'admin_announcements'

urlpatterns = [
    # 这里可能有问题，检查URL名称是否正确
    # path('admin/list/', views.AdminAnnouncementListView.as_view(), name='admin_list'),
    
    # 保留创建、编辑和删除的URL
    path('admin/create/', views.AnnouncementCreateView.as_view(), name='create'),
    path('admin/edit/<int:pk>/', views.AnnouncementUpdateView.as_view(), name='edit'),
    path('admin/delete/<int:pk>/', views.AnnouncementDeleteView.as_view(), name='delete'),
]