from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    phone = models.CharField(_('手机号码'), max_length=11, blank=True)
    avatar = models.ImageField(_('头像'), upload_to='avatars/', blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')

    def __str__(self):
        return self.username

class AdoptionApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '已通过'),
        ('rejected', '未通过'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='申请人')
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE, verbose_name='宠物')
    apply_date = models.DateTimeField(auto_now_add=True, verbose_name='申请时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    notes = models.TextField(blank=True, verbose_name='审核备注')
    contact_info = models.TextField(verbose_name='联系方式')
    experience = models.TextField(verbose_name='养宠经验')
    approve_date = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    reject_reason = models.TextField(blank=True, verbose_name='拒绝原因')
    notes = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '领养申请'
        verbose_name_plural = '领养申请'
        ordering = ['-apply_date']

    def __str__(self):
        return f"{self.user.username} 申请领养 {self.pet.name}"

