# Generated by Django 4.0.5 on 2022-06-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artmap_app', '0006_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=511),
        ),
    ]
