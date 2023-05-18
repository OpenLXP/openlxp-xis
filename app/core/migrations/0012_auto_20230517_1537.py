# Generated by Django 3.2.19 on 2023-05-17 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20220713_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataledger',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_metadata', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplementalledger',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_supplemental_data', to=settings.AUTH_USER_MODEL),
        ),
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