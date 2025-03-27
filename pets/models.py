from django.db import models
from django.utils import timezone

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    BREED_CHOICES = [
        ('中华田园猫', '中华田园猫'),
        ('布偶猫', '布偶猫'),
        ('英国短毛猫', '英国短毛猫'),
        ('波斯猫', '波斯猫'),
        ('暹罗猫', '暹罗猫'),
        ('中华田园犬', '中华田园犬'),
        ('金毛寻回犬', '金毛寻回犬'),
        ('拉布拉多', '拉布拉多'),
        ('哈士奇', '哈士奇'),
        ('柯基犬', '柯基犬'),
        ('其他', '其他'),
    ]
    breed = models.CharField(max_length=100, choices=BREED_CHOICES, verbose_name='品种')
    age = models.IntegerField()
    GENDER_CHOICES = [('M', '雄性'), ('F', '雌性')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_vaccinated = models.BooleanField(default=False)
    is_neutered = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pets/')
    created_at = models.DateTimeField(auto_now_add=True)
    health_status = models.TextField(verbose_name='健康描述', blank=True)
    description = models.TextField(verbose_name='详细描述', blank=True)
    is_adopted = models.BooleanField(default=False, verbose_name='是否被领养')
    rescue_date = models.DateField(verbose_name='救助时间', null=True, blank=True)
    rescue_story = models.TextField(verbose_name='救助故事', blank=True)
    STATUS_CHOICES = [
        ('available', '可领养'),
        ('adopted', '已领养'),
        ('medical', '医疗中')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name='状态'
    )
    arrival_date = models.DateField(
        verbose_name='收容日期',
        default=timezone.now,  # 默认当前日期
        help_text='宠物被收容的日期'
    )

    def __str__(self):
        return self.name

    def get_gender_display(self):
        return dict(self.GENDER_CHOICES).get(self.gender, '')
