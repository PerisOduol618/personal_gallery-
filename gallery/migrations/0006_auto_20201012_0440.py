# Generated by Django 2.2.8 on 2020-10-12 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20201011_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='photo_name',
            new_name='name',
        ),
    ]