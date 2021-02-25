from django.db import models
from django.urls import reverse
from django.forms import ValidationError


class XISConfiguration(models.Model):
    """Model for XIS Configuration """

    target_schema = models.CharField(
        default='p2881_schema.json', max_length=200,
        help_text='Enter the target '
                  'schema file to '
                  'validate from.')

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


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True)
    provider_name = models.CharField(max_length=255, blank=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.CharField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_hash = models.CharField(max_length=200)
    metadata = models.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_validated = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(
        max_length=10, blank=True, choices=METADATA_VALIDATION_CHOICES)


class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_hash = models.TextField(max_length=200)
    metadata = models.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_validated = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(
        max_length=10, blank=True, choices=METADATA_VALIDATION_CHOICES)


class CompositeLedger(models.Model):
    """Model for CompositeLedger"""

    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    RECORD_UPDATED_BY = [('Owner', '0'), ('System', 'S')]
    unique_record_identifier = models.CharField(max_length=50)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_transmitted = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=10, blank=True,
                                  choices=RECORD_UPDATED_BY)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_hash = models.TextField(max_length=200)
    metadata = models.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
