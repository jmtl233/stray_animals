from django.urls import path
from .views import LoginView, RegisterView, LogoutView

app_name = 'users'

urlpatterns = [
    # 登录路径（通过主URL的/login/访问）
    path('', LoginView.as_view(), name='login'),  # 实际路径为/login/
    
    # 注册路径
    path('register/', RegisterView.as_view(), name='register'),  # 实际路径为/login/register/
    
    # 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),  # 实际路径为/login/logout/
] 