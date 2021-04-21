import logging

from django.utils import timezone
from rest_framework import serializers

from core.models import MetadataLedger, SupplementalLedger
from core.utils.xss_client import \
    get_required_recommended_fields_for_validation
from core.utils.xis_internal import dict_flatten, required_recommended_logs

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Metadata Ledger"""

    class Meta:
        model = MetadataLedger

        fields = '__all__'

    def validate(self, data):
        """function to validate metadata field"""

        # Call function to get required & recommended values
        required_column_list, recommended_column_list = \
            get_required_recommended_fields_for_validation()
        json_metadata = data.get('metadata')
        validation_result = 'Y'
        record_status_result = 'Active'
        flattened_source_data = dict_flatten(json_metadata,
                                             required_column_list)
        #  looping through elements in the metadata
        for item in flattened_source_data:
            # validate for required values in data
            if item in required_column_list:
                # update validation and record status for invalid data
                # Log out error for missing required values
                if not flattened_source_data[item]:
                    validation_result = 'N'
                    record_status_result = 'Inactive'
                    required_recommended_logs(data.unique_record_identifier,
                                              "Required", item)
            # validate for recommended values in data
            elif item in recommended_column_list:
                # Log out warning for missing recommended values
                if not flattened_source_data[item]:
                    required_recommended_logs(data.unique_record_identifier,
                                              "Recommended", item)

        data['metadata_validation_status'] = validation_result
        data['record_status'] = record_status_result
        data['date_validated'] = timezone.now()

        return data

    def update(self, instance, validated_data):
        """Updates the older record in table based on validation result"""

        # Check if older record is the same to skip updating
        if validated_data['metadata_hash'] != self.instance.metadata_hash:
            if validated_data.get('record_status') == 'Active':
                # Updating old instance of record INACTIVE if present record is
                # ACTIVE
                logger.info("Active instance found for update to inactive")
                instance.record_status = 'Inactive'
                instance.date_deleted = timezone.now()
        instance.save()
        return instance

    def create(self, validated_data):
        """creates new record in table"""

        # Updating date inserted value for newly saved values
        validated_data['date_inserted'] = timezone.now()
        # Updating deleted_date for newly saved inactive values
        if validated_data.get('record_status') == "Inactive":
            validated_data['date_deleted'] = timezone.now()
        # Creating new value in metadata ledger
        try:
            # Here is the important part! Creating new object!
            instance = MetadataLedger.objects.create(**validated_data)
        except TypeError:
            raise TypeError('Cannot create record')

        return instance

    def save(self):
        """Save function to create and update record in metadata ledger """

        logger.info('Entering save function')

        # Assigning validated data as dictionary for updates in records
        validated_data = dict(
            list(self.validated_data.items())
        )

        # If value to update is present in metadata ledger
        if self.instance is not None:

            logger.info('Instance for update found')
            self.instance = self.update(self.instance, validated_data)
            # Creating new value in metadata ledger after checking duplication
            if validated_data['metadata_hash'] != self.instance.metadata_hash:
                # validated_data =self.set_validated_data(self,validated_data)
                self.instance = self.create(validated_data)

        # Update table with new record
        else:

            self.instance = self.create(validated_data)

        logger.info(self.instance)
        return self.instance


class SupplementalLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Supplemental Ledger"""

    class Meta:
        model = SupplementalLedger

        fields = '__all__'
