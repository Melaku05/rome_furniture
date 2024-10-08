# Generated by Django 5.0.1 on 2024-02-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertizementFirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertizement_first_image', models.ImageField(blank=True, null=True, upload_to='images/contacts')),
                ('advertizement_first_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='AdvertizementSecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertizement_second_image', models.ImageField(blank=True, null=True, upload_to='images/contacts')),
                ('advertizement_second_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='AdvertizementThird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertizement_third_image', models.ImageField(blank=True, null=True, upload_to='images/contacts')),
                ('advertizement_third_url', models.URLField()),
            ],
        ),
    ]
