from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'is_active', 'image']  # 修改字段
        
        labels = {
            'title': '活动标题',
            'description': '活动描述',
            'location': '活动地点',
            'start_date': '开始时间',    # 修改标签
            'end_date': '结束时间',     # 新增标签
            'is_active': '是否激活',
            'image': '活动图片'
        }
        
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }