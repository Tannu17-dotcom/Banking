# Generated by Django 3.2.4 on 2021-06-10 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_transaction_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Date_Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]