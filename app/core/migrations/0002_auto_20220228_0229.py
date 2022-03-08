# Generated by Django 3.2.12 on 2022-02-28 02:29

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataledger',
            name='updated_by',
            field=models.CharField(blank=True, choices=[('Owner', '0'), ('System', 'S')], default='System', max_length=10),
        ),
        migrations.AddField(
            model_name='supplementalledger',
            name='updated_by',
            field=models.CharField(blank=True, choices=[('Owner', '0'), ('System', 'S')], default='System', max_length=10),
        ),
        migrations.AlterField(
            model_name='compositeledger',
            name='unique_record_identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
