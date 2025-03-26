# Generated by Django 3.2.25 on 2025-03-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20250324_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(choices=[('中华田园猫', '中华田园猫'), ('布偶猫', '布偶猫'), ('英国短毛猫', '英国短毛猫'), ('波斯猫', '波斯猫'), ('暹罗猫', '暹罗猫'), ('中华田园犬', '中华田园犬'), ('金毛寻回犬', '金毛寻回犬'), ('拉布拉多', '拉布拉多'), ('哈士奇', '哈士奇'), ('柯基犬', '柯基犬'), ('其他', '其他')], max_length=100, verbose_name='品种'),
        ),
    ]
