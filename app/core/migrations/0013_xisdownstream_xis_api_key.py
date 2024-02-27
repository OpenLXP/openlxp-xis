# Generated by Django 3.2.19 on 2023-05-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230517_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='xisdownstream',
            name='xis_api_key',
            field=models.CharField(default='INVALID KEY', help_text='Enter the XIS API Key', max_length=40),
            preserve_default=False,
        ),
    ]