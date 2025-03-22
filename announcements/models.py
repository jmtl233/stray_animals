from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    is_published = models.BooleanField(default=True, verbose_name='发布状态')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告列表'

    def __str__(self):
        return self.title 