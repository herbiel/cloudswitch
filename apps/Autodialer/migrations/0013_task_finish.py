# Generated by Django 3.2.11 on 2022-01-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autodialer', '0012_alter_task_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finish',
            field=models.BooleanField(default=False, verbose_name='是否完成'),
        ),
    ]
