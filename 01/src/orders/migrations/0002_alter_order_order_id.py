# Generated by Django 3.2.5 on 2021-11-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
    ]
