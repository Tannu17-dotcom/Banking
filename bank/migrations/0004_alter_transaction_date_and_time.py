# Generated by Django 3.2.4 on 2021-06-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20210609_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Date_and_time',
            field=models.DateTimeField(),
        ),
    ]