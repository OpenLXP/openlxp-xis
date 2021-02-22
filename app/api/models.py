from django.db import models


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50)
    provider_name = models.CharField(max_length=255, blank=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.CharField(max_length=200)
    metadata_hash = models.CharField(max_length=200)
    metadata = models.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    metadata_validation_date = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(max_length=10, blank=True,
                                                  choices=
                                                  METADATA_VALIDATION_CHOICES)

class SupplementalLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField(max_length=200)
    metadata_hash = models.TextField(max_length=200)
    metadata = models.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    metadata_validation_date = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(max_length=10, blank=True,
                                                  choices=
                                                  METADATA_VALIDATION_CHOICES)