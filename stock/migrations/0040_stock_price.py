# Generated by Django 4.1.7 on 2023-04-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0039_valueofassenment'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
