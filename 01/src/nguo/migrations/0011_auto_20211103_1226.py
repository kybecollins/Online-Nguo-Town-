# Generated by Django 3.2.5 on 2021-11-03 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nguo', '0010_alter_clothes_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='clothes',
            unique_together={('title', 'slug')},
        ),
    ]
