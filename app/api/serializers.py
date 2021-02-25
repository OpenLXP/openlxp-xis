from django.utils import timezone
import logging
from rest_framework import serializers
from api.models import MetadataLedger, SupplementalLedger
from core.utils.utils import \
    get_required_recommended_fields_for_target_validation

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerSerializer(serializers.ModelSerializer):
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
        validation_result = 'Y'
        for column in json_metadata:
            required_columns = required_dict[column]
            recommended_columns = recommended_dict[column]
            for key in json_metadata[column]:
                if key in required_columns:
                    if not json_metadata[column][key]:
                        logger.info(
                            "Record " + str(
                                data.get('unique_record_identifier')
                            ) + "does not have all "
                                "REQUIRED "
                                "fields. " + key + "field"
                                                   " is "
                                                   " empty")
                        validation_result = 'N'
                    if key in recommended_columns:
                        if not json_metadata[column][key]:
                            logger.info(
                                "Record " + str(
                                    data.unique_record_identifier) +
                                " does not have all RECOMMENDED fields. " +
                                key + " field is empty")
            data['metadata_validation_status'] = validation_result
            data['metadata_validation_date'] = timezone.now()
        logger.info('The metadata validation status is ',data['metadata_validation_status'])
        return data


class SupplementalLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Supplemental Ledger"""

    class Meta:
        model = SupplementalLedger
        fields = ['unique_record_identifier',
                  'agent_name',
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
                  'metadata_validation_status']
