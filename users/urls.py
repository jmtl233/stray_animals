from django.urls import path
from .views import LoginView, RegisterView, LogoutView, UserDetailView, UserDeleteView, UserProfileView

app_name = 'users'

urlpatterns = [
    # 登录路径（通过主URL的/users/访问）
    path('login/', LoginView.as_view(), name='login'),  # 实际路径为/users/login/
    
    # 注册路径
    path('register/', RegisterView.as_view(), name='register'),  # 路径为/users/register/
    
    # 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),  # 路径为/users/logout/
    
    # 用户详情
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    
    # 删除用户
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    
    # 用户个人中心
    path('profile/', UserProfileView.as_view(), name='profile'),
] 