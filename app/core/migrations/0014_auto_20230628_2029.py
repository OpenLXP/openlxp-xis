# Generated by Django 3.2.19 on 2023-06-28 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_xisdownstream_xis_api_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataledger',
            name='metadata',
            field=models.JSONField(blank=True, validators=[django.core.validators.RegexValidator(message='Wrong Format Entered', regex='(?!(\\A( \\x09\\x0A\\x0D\\x20-\\x7E # ASCII | \\xC2-\\xDF # non-overlong 2-byte | \\xE0\\xA0-\\xBF # excluding overlongs | \\xE1-\\xEC\\xEE\\xEF{2} # straight 3-byte | \\xED\\x80-\\x9F # excluding surrogates | \\xF0\\x90-\\xBF{2} # planes 1-3 | \\xF1-\\xF3{3} # planes 4-15 | \\xF4\\x80-\\x8F{2} # plane 16 )*\\Z))')]),
        ),
        migrations.AlterField(
            model_name='supplementalledger',
            name='metadata',
            field=models.JSONField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Wrong Format Entered', regex='(?!(\\A( \\x09\\x0A\\x0D\\x20-\\x7E # ASCII | \\xC2-\\xDF # non-overlong 2-byte | \\xE0\\xA0-\\xBF # excluding overlongs | \\xE1-\\xEC\\xEE\\xEF{2} # straight 3-byte | \\xED\\x80-\\x9F # excluding surrogates | \\xF0\\x90-\\xBF{2} # planes 1-3 | \\xF1-\\xF3{3} # planes 4-15 | \\xF4\\x80-\\x8F{2} # plane 16 )*\\Z))')]),
        ),
    ]
