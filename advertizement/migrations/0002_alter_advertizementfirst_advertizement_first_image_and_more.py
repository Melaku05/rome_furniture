# Generated by Django 5.0.1 on 2024-02-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertizement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertizementfirst',
            name='advertizement_first_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/advertizements'),
        ),
        migrations.AlterField(
            model_name='advertizementsecond',
            name='advertizement_second_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/advertizements'),
        ),
        migrations.AlterField(
            model_name='advertizementthird',
            name='advertizement_third_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/advertizements'),
        ),
    ]
