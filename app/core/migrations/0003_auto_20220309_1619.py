# Generated by Django 3.2.12 on 2022-03-09 16:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220222_1547'),
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
