from rest_framework import serializers
from metadat_api import models

class TestObjectSerializer(serializers.Serializer):
    """Serializes a sample JSON object"""
    name = serializers.CharField()
    age = serializers.IntegerField()
    occupation = serializers.CharField()


# 1. MetadataLedgerSerializer
class MetadataLedgerSerializer(serializers.Serializer):
    """Serializes an entry into the Metadata Ledger"""
    model = models.MetadataLedger
    fields = ('unique_record_identifier',
              'agent_name',
              'date_inserted',
              'metadata_key',
              'metadata_hash',
              'metadata',
              'record_status',
              'date_deleted',
              'metadata_validation_date',
              'metadata_validation_status')
    extra_kwargs: {
        'unique_record_identifier': {}
    }
# 2. SupplementalLedgerSerializer



    unique_record_identifier = models.CharField(max_length=50,
                                                primary_key=True,
                                                editable=False)
    agent_name = models.CharField(max_length=255)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata_key = models.TextField()
    metadata_hash = models.TextField(max_length=200)
    metadata = modles.JSONField(blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    metadata_validation_date = models.DateTimeField(blank=True, null=True)
    metadata_validation_status = models.CharField(max_length=10, blank=True,
                                                  choices=
                                                  METADATA_VALIDATION_CHOICES)
