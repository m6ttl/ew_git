# Generated by Django 2.0.1 on 2018-10-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180114_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='易维科技', max_length=100, verbose_name='地址'),
        ),
    ]
