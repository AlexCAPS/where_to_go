# Generated by Django 4.0.5 on 2022-06-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artmap_app', '0003_place_details_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='details_url',
        ),
    ]
