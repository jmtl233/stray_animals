from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='用户名/手机号',
        error_messages={
            'required': '请输入用户名',
            'invalid': '请输入有效的用户名',
        }
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
        error_messages={
            'required': '请输入密码',
        }
    )

class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': '两次输入的密码不匹配',
    }
    
    username = forms.CharField(
        error_messages={
            'unique': '该用户名已被注册',
            'required': '请输入用户名',
        }
    )
    
    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']