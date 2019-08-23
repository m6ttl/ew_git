# Generated by Django 2.0.1 on 2018-08-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ewPresales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('owner', models.CharField(blank=True, max_length=20, null=True, verbose_name='所有人')),
                ('typen', models.CharField(blank=True, max_length=20, null=True, verbose_name='业务类型')),
                ('builder', models.CharField(blank=True, max_length=10, null=True, verbose_name='创建人')),
                ('builder_date', models.DateTimeField(blank=True, null=True, verbose_name='创建日期')),
                ('modi_man', models.CharField(blank=True, max_length=10, null=True, verbose_name='修改人')),
                ('modi_date', models.DateTimeField(blank=True, null=True, verbose_name='修改日期')),
                ('dept', models.CharField(blank=True, max_length=40, null=True, verbose_name='所属部门')),
                ('prj_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='销售机会名称')),
                ('need_finish_date', models.DateTimeField(blank=True, null=True, verbose_name='要求完成时间')),
                ('flow_n', models.CharField(blank=True, max_length=30, null=True, verbose_name='工作流阶段名称')),
                ('feedback', models.CharField(blank=True, max_length=40, null=True, verbose_name='完成效果反馈')),
                ('status', models.CharField(blank=True, max_length=30, null=True, verbose_name='售前任务单状态')),
                ('mayer_word', models.CharField(blank=True, max_length=100, null=True, verbose_name='售前主要工作')),
                ('do_s', models.CharField(blank=True, max_length=40, null=True, verbose_name='审批状态')),
                ('presales_man', models.CharField(blank=True, max_length=100, null=True, verbose_name='售前负责人')),
                ('presales_plan', models.CharField(blank=True, max_length=4096, null=True, verbose_name='本次售前策略')),
                ('m1', models.CharField(blank=True, max_length=10, null=True)),
                ('m2', models.CharField(blank=True, max_length=10, null=True)),
                ('m3', models.CharField(blank=True, max_length=10, null=True)),
                ('m4', models.CharField(blank=True, max_length=10, null=True)),
                ('m5', models.CharField(blank=True, max_length=10, null=True)),
                ('m6', models.CharField(blank=True, max_length=10, null=True)),
                ('m7', models.CharField(blank=True, max_length=10, null=True)),
                ('m8', models.CharField(blank=True, max_length=10, null=True)),
                ('m9', models.CharField(blank=True, max_length=10, null=True)),
                ('m10', models.CharField(blank=True, max_length=10, null=True)),
                ('n1', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n2', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n3', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n4', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n5', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n6', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n7', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('n8', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'verbose_name': '售前任务单',
                'verbose_name_plural': '售前任务单',
            },
        ),
    ]
