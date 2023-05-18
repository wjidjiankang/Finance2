# Generated by Django 4.1.2 on 2022-10-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0017_delete_fund_delete_stock_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=10)),
                ('mark', models.CharField(max_length=4)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amt', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=10)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amt', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
