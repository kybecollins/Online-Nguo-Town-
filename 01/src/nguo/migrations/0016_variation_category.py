# Generated by Django 3.2.5 on 2021-11-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguo', '0015_variation_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], default='size', max_length=150),
        ),
    ]
