# Generated by Django 4.2.7 on 2023-12-05 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 5, 19, 56, 38, 61520, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата оплаты'),
        ),
    ]