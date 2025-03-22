from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # 暂时留空或添加测试路由
    path('test/', views.test_view, name='test'),
    # 新增list路由
    path('list/', views.PetListView.as_view(), name='list'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='detail'),
] 