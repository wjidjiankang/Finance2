# Generated by Django 4.1.2 on 2022-11-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0021_delete_fund_rename_amt_stock_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinhand',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
