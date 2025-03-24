# Generated by Django 3.2.25 on 2025-03-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_is_adopted'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='rescue_date',
            field=models.DateField(blank=True, null=True, verbose_name='救助时间'),
        ),
        migrations.AddField(
            model_name='pet',
            name='rescue_story',
            field=models.TextField(blank=True, verbose_name='救助故事'),
        ),
    ]
