# Generated by Django 4.2.7 on 2023-12-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_owner_delete_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='telegram id'),
        ),
    ]
