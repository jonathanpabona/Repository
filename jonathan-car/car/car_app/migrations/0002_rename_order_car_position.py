# Generated by Django 5.0.4 on 2024-04-18 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='order',
            new_name='position',
        ),
    ]