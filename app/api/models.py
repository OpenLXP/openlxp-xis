from django.db import models


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    unique_record_identifier = models.CharField(max_length=50)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
<<<<<<<< HEAD:app/api/models.py
# 2. SupplementalLedgerModel
========
    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True,
                                                editable=False)
<<<<<<< HEAD
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField(max_length=200)
<<<<<<< HEAD
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
=======
    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50)
<<<<<<< HEAD
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
    provider_name = models.CharField(max_length=255, blank=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.CharField(max_length=200)
    metadata_hash = models.CharField(max_length=200)
<<<<<<< HEAD
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    metadata = models.JSONField(blank=True)
>>>>>>> 82a35a5 (fixed model typos, added connection to xia network)
=======
=======
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
    provider_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField()
<<<<<<< HEAD
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
    metadata = models.JSONField(blank=True)
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
=======
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField(max_length=200)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aaa8cae (Commits before rebase)
=======
=======
    unique_record_identifier = models.CharField(max_length=50, primary_key= True)
>>>>>>> 074b4b6 (Adding models.py: Made unique_record_identifier as primary key to avoid duplications)
=======
    unique_record_identifier = models.CharField(max_length=50, primary_key=True)
>>>>>>> 3f562be (ECC-420 Refactoring code and updating urls.py)
    provider_name = models.CharField(max_length=255, blank=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.CharField(max_length=200)
    metadata_hash = models.CharField(max_length=200)
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    metadata = models.JSONField(blank=True)
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
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
                                                  METADATA_VALIDATION_CHOICES)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
<<<<<<< HEAD
    unique_record_identifier = models.CharField(max_length=50)
<<<<<<< HEAD
<<<<<<< HEAD
=======
    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True,
                                                editable=False)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
    agent_name = models.CharField(max_length=255)
=======
    provider_name = models.CharField(max_length=255)
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
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
<<<<<<< HEAD
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
    metadata = models.JSONField(blank=True)
>>>>>>> 82a35a5 (fixed model typos, added connection to xia network)
=======
    metadata = models.JSONField(blank=True)
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
=======

>>>>>>> aaa8cae (Commits before rebase)
=======
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======

>>>>>>> 074b4b6 (Adding models.py: Made unique_record_identifier as primary key to avoid duplications)
class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    unique_record_identifier = models.CharField(max_length=50)
=======

class SupplementalLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
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
=======
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
    metadata = models.JSONField(blank=True)
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
    metadata = modles.JSONField(blank=True)
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
                                                  METADATA_VALIDATION_CHOICES)


                                                  METADATA_VALIDATION_CHOICES)

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
                                                  METADATA_VALIDATION_CHOICES)
>>>>>>> aaa8cae (Commits before rebase)
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
