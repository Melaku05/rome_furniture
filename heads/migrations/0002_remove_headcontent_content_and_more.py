# Generated by Django 5.0.1 on 2024-02-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headcontent',
            name='content',
        ),
        migrations.AddField(
            model_name='headcontent',
            name='footer_meta_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='headcontent',
            name='header_meta_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
