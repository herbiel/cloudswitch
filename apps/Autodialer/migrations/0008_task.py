# Generated by Django 3.2.10 on 2022-01-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autodialer', '0007_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='', max_length=20, verbose_name='任务名称')),
                ('type', models.FloatField(choices=[('Broadcastivr', 'Broadcastivr'), ('Predictive', 'Predictive')], verbose_name='号码')),
                ('number', models.FloatField(default='', verbose_name='号码')),
                ('describe', models.FloatField(default='', verbose_name='描述')),
                ('create_time', models.DateTimeField(default='', max_length=20, verbose_name='创建时间')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
            },
        ),
    ]
