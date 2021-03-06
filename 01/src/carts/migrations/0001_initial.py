# Generated by Django 3.2.5 on 2021-11-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nguo', '0006_auto_20211101_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, null=True, to='nguo.Clothes')),
            ],
        ),
    ]
