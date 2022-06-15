# Generated by Django 3.2.13 on 2022-06-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220524_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='xisconfiguration',
            name='xss_host',
            field=models.CharField(default='', help_text='Enter the host url for the XSS (Schema Service) to use.', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='xisconfiguration',
            name='target_schema',
            field=models.CharField(default='p2881', help_text='Enter the target schema name or IRI to validate with.', max_length=200),
        ),
    ]
