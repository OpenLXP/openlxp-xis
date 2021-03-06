from django.db import models
from django.forms import ValidationError
from django.urls import reverse

from core.utils.notification import email_verification


class XISConfiguration(models.Model):
    """Model for XIS Configuration """

    target_schema = models.CharField(
        default='p2881_schema.json', max_length=200,
        help_text='Enter the target '
                  'schema file to '
                  'validate from.')
    xse_host = models.CharField(
        help_text='Enter the host url for the XSE (Search Engine) to use.',
        max_length=200
    )
    xse_index = models.CharField(
        help_text='Enter the name of the index for the XSE (Search Engine) \
            to query.',
        max_length=200
    )

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('Configuration-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk and XISConfiguration.objects.exists():
            raise ValidationError('XISConfiguration model already exists')
        return super(XISConfiguration, self).save(*args, **kwargs)


class ReceiverEmailConfiguration(models.Model):
    """Model for Email Configuration """

    email_address = models.EmailField(
        max_length=254,
        help_text='Enter email personas addresses to send log data',
        unique=True)

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('Configuration-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        email_verification(self.email_address)
        return super(ReceiverEmailConfiguration, self).save(*args, **kwargs)


class SenderEmailConfiguration(models.Model):
    """Model for Email Configuration """

    sender_email_address = models.EmailField(
        max_length=254,
        help_text='Enter sender email address to send log data from')

    def save(self, *args, **kwargs):
        if not self.pk and SenderEmailConfiguration.objects.exists():
            raise ValidationError('There can be only one '
                                  'SenderEmailConfiguration instance')
        return super(SenderEmailConfiguration, self).save(*args, **kwargs)


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    composite_ledger_transmission_date = models.DateTimeField(blank=True,
                                                              null=True)
    composite_ledger_transmission_status = \
        models.CharField(max_length=10,
                         blank=True,
                         default='N',
                         choices=METADATA_VALIDATION_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_validated = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True)
    metadata_hash = models.CharField(max_length=200)
    metadata_key = models.CharField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_validation_status = \
        models.CharField(max_length=10, blank=True,
                         choices=METADATA_VALIDATION_CHOICES)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True)


class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    agent_name = models.CharField(max_length=255)
    composite_ledger_transmission_date = models.DateTimeField(blank=True,
                                                              null=True)
    composite_ledger_transmission_status = \
        models.CharField(max_length=10,
                         blank=True,
                         default='N',
                         choices=METADATA_VALIDATION_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_validated = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True)
    metadata_hash = models.TextField(max_length=200)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_validation_status = \
        models.CharField(max_length=10, blank=True,
                         choices=METADATA_VALIDATION_CHOICES)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True)


class CompositeLedger(models.Model):
    """Model for CompositeLedger"""

    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    RECORD_UPDATED_BY = [('Owner', '0'), ('System', 'S')]
    RECORD_TRANSMISSION_STATUS_CHOICES = [('Successful', 'S'), ('Failed', 'F'),
                                          ('Pending', 'P'), ('Ready', 'R')]
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_transmitted = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True)
    metadata_hash = models.TextField(max_length=200)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_transmission_status = \
        models.CharField(max_length=10, blank=True,
                         default='Ready',
                         choices=RECORD_TRANSMISSION_STATUS_CHOICES)
    metadata_transmission_status_code = models.CharField(max_length=200,
                                                         blank=True)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True)
    updated_by = models.CharField(max_length=10, blank=True,
                                  choices=RECORD_UPDATED_BY)
