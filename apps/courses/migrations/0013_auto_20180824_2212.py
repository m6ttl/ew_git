# Generated by Django 2.0.1 on 2018-08-24 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_lesson_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='detail',
            new_name='Lessondetail',
        ),
    ]
