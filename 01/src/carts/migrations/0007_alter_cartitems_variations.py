# Generated by Django 3.2.5 on 2021-11-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguo', '0016_variation_category'),
        ('carts', '0006_cartitems_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='variations',
            field=models.ManyToManyField(blank=True, to='nguo.Variation'),
        ),
    ]
