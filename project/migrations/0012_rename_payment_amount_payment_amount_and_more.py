# Generated by Django 4.2.7 on 2023-12-15 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_course_price_alter_payment_payment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='paid_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='payment_method',
            new_name='method',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 15, 0, 10, 22, 592655, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата оплаты'),
        ),
    ]
