from django.utils import timezone
import logging
from rest_framework import serializers
from api.models import MetadataLedger
from core.utils.utils import \
    get_required_recommended_fields_for_target_validation

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerSerializer(serializers.Serializer):
    """Serializes an entry into the Metadata Ledger"""

    class Meta:
        model = MetadataLedger

        fields = ['unique_record_identifier',
                  'provider_name',
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
                  'metadata_validation_status']

    def validate(self, data):
        """function to validate metadata field"""

        # Call function to get required & recommended values
        required_dict, recommended_dict = \
            get_required_recommended_fields_for_target_validation()
        json_metadata = data.get('metadata')
        for column in json_metadata:
            required_columns = required_dict[column]
            recommended_columns = recommended_dict[column]
            validation_result = 'Y'
            for key in json_metadata[column]:
                if key in required_columns:
                    if not json_metadata[column][key]:
                        validation_result = 'N'
                        logger.info(
                            "Record " + str(
                                data.get('unique_record_identifier')
                            ) + "does not have all "
                                "REQUIRED "
                                "fields. " + key + "field"
                                                   " is "
                                                   " empty")
                    if key in recommended_columns:
                        if not json_metadata[column][key]:
                            logger.info(
                                "Record " + str(
                                    data.unique_record_identifier) +
                                " does not have all RECOMMENDED fields. " +
                                key + " field is empty")
        data['metadata_validation_status'] = validation_result
        data['metadata_validation_date'] = timezone.now()
        logger.info(data['metadata_validation_status'],
                    data['metadata_validation_date'])
        return data

# class SupplementalLedgerSerializer(serializers.Serializer):
#     """Serializes an entry into the Supplemental Ledger"""
#
#     class Meta:
#         model = SupplementalLedger
#         fields = ('unique_record_identifier',
#                   'agent_name',
#                   'date_inserted',
#                   'metadata_key',
#                   'metadata_hash',
#                   'metadata',
#                   'record_status',
#                   'date_deleted',
#                   'metadata_validation_date',
#                   'metadata_validation_status')
#         extra_kwargs:{
#             'unique_record_identifier': {'max_length': 50},
#             'agent_name': {'max_length': 255},
#             'date_inserted': {'blank': True, 'null': True},
#             'metadata_hash': {'max_length': 200},
#             'metadata': {'blank': True},
#             'record_status': {'max_length': 10,
#                               'blank': True,
#                               'choices': SupplementalLedger.RECORD_ACTIVATION_STATUS_CHOICES
#                               },
#             'date_deleted': {'blank': True, 'null': True},
#             'metadata_validation_date': {'blank': True, 'null': True},
#             'metadata_validation_status': {'max_length': 10,
#                                            'blank': True,
#                                            'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES}
#         }
