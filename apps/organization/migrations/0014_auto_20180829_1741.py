# Generated by Django 2.0.1 on 2018-08-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_auto_20180829_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='1@ewide.net', max_length=50, verbose_name='邮箱'),
        ),
    ]
