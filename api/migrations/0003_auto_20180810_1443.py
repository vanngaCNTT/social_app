# Generated by Django 2.0.5 on 2018-08-10 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180810_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='like',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
    ]
