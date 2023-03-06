# Generated by Django 3.2 on 2023-03-04 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_menu_parent_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='menu.menu', verbose_name='Главное меню'),
        ),
    ]
