# Generated by Django 5.0.1 on 2024-02-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='facebook_url',
            field=models.URLField(blank=True, default='#', verbose_name='facebook url'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram_url',
            field=models.URLField(blank=True, default='#', verbose_name='telegram url'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='whatsapp_url',
            field=models.URLField(blank=True, default='#', verbose_name='whatsapp url'),
        ),
    ]
