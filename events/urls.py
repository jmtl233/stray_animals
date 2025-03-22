from django.urls import path
from . import views

app_name = 'events'  # 添加应用命名空间
urlpatterns = [
    path('', views.event_list, name='list'),  # 创建事件列表路由
] 