# Generated by Django 5.0.1 on 2024-04-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='username'),
        ),
    ]
