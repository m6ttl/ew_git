# Generated by Django 2.0.1 on 2018-12-25 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ewproject', '0011_auto_20181225_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_month', models.CharField(default='2019/01', max_length=20, verbose_name='月份')),
                ('kind', models.CharField(blank=True, choices=[('首付款', '首付款'), ('启动款', '启动款'), ('上线款', '上线款'), ('验收款', '验收款'), ('质保款', '质保款')], max_length=40, null=True, verbose_name='类型')),
                ('builder', models.CharField(blank=True, max_length=10, null=True, verbose_name='登记人')),
                ('build_date', models.DateField(blank=True, null=True, verbose_name='发生日期')),
                ('pay', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='金额')),
            ],
            options={
                'verbose_name': '项目回款',
                'verbose_name_plural': '项目回款',
            },
        ),
        migrations.AlterField(
            model_name='ewproject',
            name='bargain_m',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='合同金额'),
        ),
        migrations.AlterField(
            model_name='ewproject',
            name='task_m',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='任务单金额'),
        ),
        migrations.AddField(
            model_name='projectreceived',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ewproject.ewProject', verbose_name='项目'),
        ),
    ]
