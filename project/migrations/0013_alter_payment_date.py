# Generated by Django 4.2.7 on 2023-12-15 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_rename_payment_amount_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 15, 0, 17, 44, 997548, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата оплаты'),
        ),
    ]