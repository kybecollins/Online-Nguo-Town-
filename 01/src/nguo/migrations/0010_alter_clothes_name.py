# Generated by Django 3.2.5 on 2021-11-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguo', '0009_auto_20211103_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
