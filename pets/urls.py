from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # 暂时留空或添加测试路由
    path('test/', views.test_view, name='test'),
    # 新增list路由
    path('list/', views.PetListView.as_view(), name='list'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='detail'),
    path('create/', views.PetCreateView.as_view(), name='create'),  # 新增创建路由
    path('<int:pk>/edit/', views.PetUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PetDeleteView.as_view(), name='delete'),  # 新增删除路由
] 