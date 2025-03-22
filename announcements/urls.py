from django.urls import path
from . import views

app_name = 'admin_announcements'

urlpatterns = [
    path('admin/list/', views.AdminAnnouncementListView.as_view(), name='admin_list'),
] 