from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeLedger',
            fields=[
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('date_inserted', models.DateTimeField(blank=True, null=True)),
                ('date_transmitted', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True)),
                ('metadata_hash', models.TextField(max_length=200)),
                ('metadata_key', models.TextField(max_length=200)),
                ('metadata_key_hash', models.CharField(max_length=200)),
                ('metadata_transmission_status', models.CharField(blank=True, choices=[('Successful', 'S'), ('Failed', 'F'), ('Pending', 'P'), ('Ready', 'R')], default='Ready', max_length=10)),
                ('metadata_transmission_status_code', models.CharField(blank=True, max_length=200)),
                ('provider_name', models.CharField(blank=True, max_length=255)),
                ('record_status', models.CharField(blank=True, choices=[('Active', 'A'), ('Inactive', 'I')], max_length=10)),
                ('unique_record_identifier', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('updated_by', models.CharField(blank=True, choices=[('Owner', '0'), ('System', 'S')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MetadataLedger',
            fields=[
                ('composite_ledger_transmission_date', models.DateTimeField(blank=True, null=True)),
                ('composite_ledger_transmission_status', models.CharField(blank=True, choices=[('Successful', 'S'), ('Failed', 'F'), ('Pending', 'P'), ('Ready', 'R')], default='Ready', max_length=10)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('date_inserted', models.DateTimeField(blank=True, null=True)),
                ('date_validated', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True)),
                ('metadata_hash', models.CharField(max_length=200)),
                ('metadata_key', models.CharField(max_length=200)),
                ('metadata_key_hash', models.CharField(max_length=200)),
                ('metadata_validation_status', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('provider_name', models.CharField(blank=True, max_length=255)),
                ('record_status', models.CharField(blank=True, choices=[('Active', 'A'), ('Inactive', 'I')], max_length=10)),
                ('unique_record_identifier', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiverEmailConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(help_text='Enter email personas addresses to send log data', max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SenderEmailConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email_address', models.EmailField(help_text='Enter sender email address to send log data from', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SupplementalLedger',
            fields=[
                ('composite_ledger_transmission_date', models.DateTimeField(blank=True, null=True)),
                ('composite_ledger_transmission_status', models.CharField(blank=True, choices=[('Successful', 'S'), ('Failed', 'F'), ('Pending', 'P'), ('Ready', 'R')], default='Ready', max_length=10)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('date_inserted', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True)),
                ('metadata_hash', models.TextField(max_length=200)),
                ('metadata_key', models.TextField(max_length=200)),
                ('metadata_key_hash', models.CharField(max_length=200)),
                ('provider_name', models.CharField(blank=True, max_length=255)),
                ('record_status', models.CharField(blank=True, choices=[('Active', 'A'), ('Inactive', 'I')], max_length=10)),
                ('unique_record_identifier', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='XISConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_schema', models.CharField(default='p2881_schema.json', help_text='Enter the target schema file to validate from.', max_length=200)),
                ('xse_host', models.CharField(help_text='Enter the host url for the XSE (Search Engine) to use.', max_length=200)),
                ('xse_index', models.CharField(help_text='Enter the name of the index for the XSE (Search Engine)             to query.', max_length=200)),
            ],
        ),
    ]