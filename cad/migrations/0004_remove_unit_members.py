# Generated by Django 4.1.7 on 2023-02-21 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cad', '0003_unit_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='members',
        ),
    ]