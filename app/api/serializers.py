import logging

from django.utils import timezone
from rest_framework import serializers

from core.models import MetadataLedger, SupplementalLedger
from core.utils.utils import \
    get_required_recommended_fields_for_target_validation

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Metadata Ledger"""

    class Meta:
        model = MetadataLedger

        fields = '__all__'

    def validate(self, data):
        """function to validate metadata field"""

        # Call function to get required & recommended values
        required_dict, recommended_dict = \
            get_required_recommended_fields_for_target_validation()
        json_metadata = data.get('metadata')
        validation_result = 'Y'
        record_status_result = 'Active'
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
                        record_status_result = 'Inactive'
                        validation_result = 'N'
                    if key in recommended_columns:
                        if not json_metadata[column][key]:
                            logger.info(
                                "Record " + str(
                                    data.unique_record_identifier) +
                                " does not have all RECOMMENDED fields. " +
                                key + " field is empty")
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
