from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='用户名/手机号')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2') 