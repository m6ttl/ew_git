# Generated by Django 2.0.1 on 2018-01-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='国内名校', max_length=10, verbose_name='类型标签'),
        ),
    ]
