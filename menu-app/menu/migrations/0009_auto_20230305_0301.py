# Generated by Django 3.2 on 2023-03-05 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_menu_parent_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent_menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='explicit_url',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]