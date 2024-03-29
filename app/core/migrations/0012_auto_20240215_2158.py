# Generated by Django 3.2.24 on 2024-02-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220713_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xisdownstream',
            name='xis_api_endpoint',
            field=models.CharField(help_text='Enter the XIS Instance API endpoint', max_length=200),
        ),
        migrations.AlterField(
            model_name='xisupstream',
            name='xis_api_endpoint',
            field=models.CharField(help_text='Enter the XIS Instance API endpoint', max_length=200),
        ),
    ]
