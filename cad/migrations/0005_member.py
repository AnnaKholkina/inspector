# Generated by Django 4.1.7 on 2023-02-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cad', '0004_remove_unit_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
