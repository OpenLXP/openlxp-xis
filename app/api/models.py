from django.db import models


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

<<<<<<< HEAD
    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
<<<<<<< HEAD
    unique_record_identifier = models.CharField(max_length=50)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<<< HEAD:app/api/models.py
# 2. SupplementalLedgerModel
========
    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True,
                                                editable=False)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField(max_length=200)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    metadata = models.JSONField(blank=True)
=======
    metadata = modles.JSONField(blank=True)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
=======
=======
    unique_record_identifier = models.CharField(max_length=50, primary_key= True)
>>>>>>> 074b4b6 (Adding models.py: Made unique_record_identifier as primary key to avoid duplications)
    provider_name = models.CharField(max_length=255, blank=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.CharField(max_length=200)
    metadata_hash = models.CharField(max_length=200)
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    metadata = models.JSONField(blank=True)
>>>>>>> 82a35a5 (fixed model typos, added connection to xia network)
=======
=======
    provider_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField()
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
    metadata = models.JSONField(blank=True)
>>>>>>> 01f0bef (Update models.py and serializers.py)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    metadata_validation_date = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(max_length=10, blank=True,
                                                  choices=
                                                  METADATA_VALIDATION_CHOICES)


class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
<<<<<<< HEAD
    unique_record_identifier = models.CharField(max_length=50)
<<<<<<< HEAD
=======
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True,
                                                editable=False)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField(max_length=200)
    metadata_hash = models.TextField(max_length=200)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    metadata = models.JSONField(blank=True)
=======
    metadata = modles.JSONField(blank=True)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
=======
    provider_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField()
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
    metadata = models.JSONField(blank=True)
>>>>>>> 82a35a5 (fixed model typos, added connection to xia network)
=======
    metadata = models.JSONField(blank=True)
>>>>>>> 01f0bef (Update models.py and serializers.py)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    metadata_validation_date = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(max_length=10, blank=True,
                                                  choices=
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                                                  METADATA_VALIDATION_CHOICES)
=======
                                                  METADATA_VALIDATION_CHOICES)
>>>>>>>> 21f2f28 (added new core app; fixed secret key docker config):app/metadata_api/models.py
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
                                                  METADATA_VALIDATION_CHOICES)
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======
                                                  METADATA_VALIDATION_CHOICES)
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
