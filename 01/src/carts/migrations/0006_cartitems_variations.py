# Generated by Django 3.2.5 on 2021-11-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguo', '0016_variation_category'),
        ('carts', '0005_cartitems_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='nguo.Variation'),
        ),
    ]
