# Generated by Django 4.2.7 on 2023-12-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_telegram_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram_id',
        ),
    ]
