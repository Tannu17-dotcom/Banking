# Generated by Django 3.2.4 on 2021-06-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_rename_acc_no_of_sender_transaction_acc_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Acc_No',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Current_Balance',
            field=models.IntegerField(),
        ),
    ]