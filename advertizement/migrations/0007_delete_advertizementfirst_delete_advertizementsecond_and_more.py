# Generated by Django 5.0.1 on 2024-08-19 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertizement', '0006_alter_favicon_favicon_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdvertizementFirst',
        ),
        migrations.DeleteModel(
            name='AdvertizementSecond',
        ),
        migrations.DeleteModel(
            name='AdvertizementThird',
        ),
    ]
