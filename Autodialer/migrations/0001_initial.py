# Generated by Django 3.2.5 on 2021-12-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastPlayback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='', max_length=20, verbose_name='任务名称')),
                ('start_time', models.DateTimeField(default='', max_length=20, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default='', max_length=20, verbose_name='结束时间')),
                ('broadcastPlaybackUri', models.CharField(default='', max_length=200, verbose_name='语音文件url')),
                ('fail_retry_time', models.CharField(default='', max_length=20, verbose_name='失败重试次数')),
                ('enable', models.BooleanField(default=False, verbose_name='启用')),
            ],
            options={
                'verbose_name': 'BroadcastPlayback',
                'verbose_name_plural': 'BroadcastPlayback',
            },
        ),
    ]