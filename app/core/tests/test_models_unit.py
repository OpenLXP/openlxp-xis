from core.models import MetadataLedger, XISConfiguration
from django.test import SimpleTestCase, tag


@tag('unit')
class ModelTests(SimpleTestCase):

    def test_create_xis_configuration(self):
        """Test that creating a new XIS Configuration entry is successful
        with defaults """
        target_schema = 'test_file.json'

        xisConfig = XISConfiguration(target_schema=target_schema)

        self.assertEqual(xisConfig.target_schema,
                         target_schema)

    def test_metadata_ledger(self):
        """Test for a new Metadata_Ledger entry is successful with defaults"""

        unique_record_identifier = 'fe16decc-a982-40b2-bd2b-e8ab98b80a6e'
        provider_name = 'DAU'
        date_inserted = ''
        metadata = ''
        metadata_hash = '4f2a7da4f872e9807079ac7cb42aefb4'
        metadata_key = 'DAU_apr_06_a03_bs_enus'
        metadata_key_hash = '4f2a7da4f872e9807079ac7cb42aefb5'
        record_status = ''
        date_deleted = ''
        date_validated = ''
        metadata_validation_status = ''

        metadataLedger = MetadataLedger(
            unique_record_identifier=unique_record_identifier,
            provider_name=provider_name,
            date_inserted=date_inserted,
            metadata=metadata,
            metadata_hash=metadata_hash,
            metadata_key=metadata_key,
            metadata_key_hash=metadata_key_hash,
            record_status=record_status,
            date_deleted=date_deleted,
            date_validated=date_validated,
            metadata_validation_status=metadata_validation_status)

        self.assertEqual(metadataLedger.unique_record_identifier,
                         unique_record_identifier)
        self.assertEqual(metadataLedger.provider_name,
                         provider_name)
        self.assertEqual(metadataLedger.date_inserted,
                         date_inserted)
        self.assertEqual(metadataLedger.metadata,
                         metadata)
        self.assertEqual(metadataLedger.metadata_hash,
                         metadata_hash)
        self.assertEqual(metadataLedger.metadata_key,
                         metadata_key)
        self.assertEqual(metadataLedger.metadata_key_hash,
                         metadata_key_hash)
        self.assertEqual(metadataLedger.record_status,
                         record_status)
        self.assertEqual(metadataLedger.date_deleted,
                         date_deleted)
        self.assertEqual(metadataLedger.date_validated,
                         date_validated)
        self.assertEqual(metadataLedger.metadata_validation_status,
                         metadata_validation_status)
