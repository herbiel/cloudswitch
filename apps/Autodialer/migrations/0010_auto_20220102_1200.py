# Generated by Django 3.2.10 on 2022-01-02 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autodialer', '0009_auto_20220102_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='describe',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='number',
            field=models.IntegerField(default='', verbose_name='号码'),
        ),
    ]
