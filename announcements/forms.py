from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入公告标题'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '请输入公告内容'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'title': '公告标题',
            'content': '公告内容',
            'is_published': '立即发布'
        }