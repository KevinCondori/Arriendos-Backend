# Generated by Django 4.2.4 on 2023-11-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_property_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
