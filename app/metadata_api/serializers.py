from rest_framework import serializers
from metadata_api import models

class TestObjectSerializer(serializers.Serializer):
    """Serializes a sample JSON object"""
    name = serializers.CharField()
    age = serializers.IntegerField()
    occupation = serializers.CharField()


class MetadataLedgerSerializer(serializers.Serializer):
    """Serializes an entry into the Metadata Ledger"""
    class Meta:
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
                'unique_record_identifier': {'max_length':50,
                                             'primary_key':True,
                                             'editable':False},
                'agent_name': {'max_length':255},
                'date_inserted': {'blank':True, 'null':True},
                'metadata_hash': {'max_length':200},
                'metadata': {'blank'=True},
                'record_status': {'max_length': 10,
                                  'blank': True,
                                  'choices': RECORD_ACTIVATION_STATUS_CHOICES
                                  },
                'date_deleted': {'blank': True, 'null': True},
                'metadata_validation_date': {'blank': True, 'null': True},
                'metadata_validation_status': {'max_length': 10,
                                               'blank': True,
                                               'choices': MetadataLedger.METADATA_VALIDATION_CHOICES},
                }


class SupplementalLedgerSerializer(serializers.Serializer):
    """Serializes an entry into the Supplemental Ledger"""
    class Meta:
        model = models.SupplementalLedger
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
                'unique_record_identifier': {'max_length':50,
                                             'primary_key':True,
                                             'editable':False},
                'agent_name': {'max_length':255},
                'date_inserted': {'blank':True, 'null':True},
                'metadata_hash': {'max_length':200},
                'metadata': {'blank'=True},
                'record_status': {'max_length': 10,
                                  'blank': True,
                                  'choices': RECORD_ACTIVATION_STATUS_CHOICES
                                  },
                'date_deleted': {'blank': True, 'null': True},
                'metadata_validation_date': {'blank': True, 'null': True},
                'metadata_validation_status': {'max_length': 10,
                                               'blank': True,
                                               'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES},
                }
