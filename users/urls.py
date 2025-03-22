from django.urls import path
from . import views
from .views import LoginView

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] 