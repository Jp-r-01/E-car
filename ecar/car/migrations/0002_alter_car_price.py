# Generated by Django 4.2 on 2023-04-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(),
        ),
    ]
