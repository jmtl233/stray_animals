from django.utils import timezone
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='活动标题')
    description = models.TextField(verbose_name='活动描述')
    location = models.CharField(max_length=200, verbose_name='活动地点')
    start_date = models.DateTimeField(verbose_name='开始时间')  # 原event_date改为start_date
    end_date = models.DateTimeField(
        verbose_name='结束时间',
        default=timezone.now() + timezone.timedelta(hours=2)  # 添加默认值
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name='活动图片')
    
    @property
    def is_past_due(self):
        now = timezone.now()
        return now > self.end_date  # 修改为判断是否超过结束时间
    
    def __str__(self):
        return f"{self.title} ({self.start_date:%Y-%m-%d %H:%M})"  # 显示开始时间
    
    class Meta:
        verbose_name = '救助活动'
        verbose_name_plural = '救助活动列表'
        ordering = ['-start_date']  # 将原来的-event_date改为-start_date
    
    @property
    def is_past_due(self):
        now = timezone.now()
        return now > self.end_date
