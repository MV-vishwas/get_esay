# Generated by Django 3.0.4 on 2020-04-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_service_provide'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_provide',
            new_name='Service_provider',
        ),
    ]