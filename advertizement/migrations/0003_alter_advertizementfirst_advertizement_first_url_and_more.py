# Generated by Django 5.0.1 on 2024-02-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertizement', '0002_alter_advertizementfirst_advertizement_first_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertizementfirst',
            name='advertizement_first_url',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='advertizementsecond',
            name='advertizement_second_url',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='advertizementthird',
            name='advertizement_third_url',
            field=models.URLField(default='#'),
        ),
    ]
