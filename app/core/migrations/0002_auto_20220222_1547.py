# Generated by Django 3.2.12 on 2022-02-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xisconfiguration',
            name='autocomplete_field',
            field=models.CharField(default='metadata.Metadata_Ledger.Course.CourseTitle', help_text='Enter the field to support autocomplete on in XSE.', max_length=200),
        ),
        migrations.AddField(
            model_name='xisconfiguration',
            name='filter_field',
            field=models.CharField(default='provider_name', help_text='Enter the field to filter XSE queries by.', max_length=200),
        ),
    ]
