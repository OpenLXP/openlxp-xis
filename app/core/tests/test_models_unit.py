from django.test import SimpleTestCase, tag
from django.utils import timezone

from core.models import (CompositeLedger, MetadataLedger, SupplementalLedger,
                         XISConfiguration)


@tag('unit')
class ModelTests(SimpleTestCase):

    def test_create_xis_configuration(self):
        """Test that creating a new XIS Configuration entry is successful
        with defaults """
        target_schema = 'test_file.json'
        xse_host = 'test:8080'
        xse_index = 'test-index'

        xisConfig = XISConfiguration(target_schema=target_schema,
                                     xse_host=xse_host,
                                     xse_index=xse_index)

        self.assertEqual(xisConfig.target_schema,
                         target_schema)
        self.assertEqual(xisConfig.xse_host, xse_host)
        self.assertEqual(xisConfig.xse_index, xse_index)

    def test_metadata_ledger(self):
        """Test for a new Metadata_Ledger entry is successful with defaults"""

        unique_record_identifier = 'fe16decc-a982-40b2-bd2b-e8ab98b80a6e'
        provider_name = 'AGENT'
        date_inserted = timezone.now()
        metadata = ''
        metadata_hash = '4f2a7da4f872e9807079ac7cb42aefb4'
        metadata_key = 'Agent_test'
        metadata_key_hash = '4f2a7da4f872e9807079ac7cb42aefb5'
        record_status = ''
        date_deleted = timezone.now()
        date_validated = timezone.now()
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

    def test_supplemental_ledger(self):
        """Test for a new Supplemental_Ledger entry is successful with
        defaults """

        unique_record_identifier = 'fe16decc-a982-40b2-bd2b-e8ab98b80a6e'
        provider_name = 'AGENT'
        date_inserted = ''
        metadata = ''
        metadata_hash = '4f2a7da4f872e9807079ac7cb42aefb4'
        metadata_key = 'AGENT_Test_key'
        metadata_key_hash = '4f2a7da4f872e9807079ac7cb42aefb5'
        record_status = ''
        date_deleted = timezone.now()
        date_validated = timezone.now()
        metadata_validation_status = ''

        supplemental_ledger = SupplementalLedger(
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

        self.assertEqual(supplemental_ledger.unique_record_identifier,
                         unique_record_identifier)
        self.assertEqual(supplemental_ledger.provider_name,
                         provider_name)
        self.assertEqual(supplemental_ledger.date_inserted,
                         date_inserted)
        self.assertEqual(supplemental_ledger.metadata,
                         metadata)
        self.assertEqual(supplemental_ledger.metadata_hash,
                         metadata_hash)
        self.assertEqual(supplemental_ledger.metadata_key,
                         metadata_key)
        self.assertEqual(supplemental_ledger.metadata_key_hash,
                         metadata_key_hash)
        self.assertEqual(supplemental_ledger.record_status,
                         record_status)
        self.assertEqual(supplemental_ledger.date_deleted,
                         date_deleted)
        self.assertEqual(supplemental_ledger.date_validated,
                         date_validated)
        self.assertEqual(supplemental_ledger.metadata_validation_status,
                         metadata_validation_status)

    def test_composite_ledger(self):
        """Test for a new Composite_Ledger entry is successful with defaults"""

        unique_record_identifier = 'fe16decc-a982-40b2-bd2b-e8ab98b80a6e'
        provider_name = 'AGENT'
        date_inserted = timezone.now()
        metadata = ''
        metadata_hash = '4f2a7da4f872e9807079ac7cb42aefb4'
        metadata_key = 'AGENT_Test_key'
        metadata_key_hash = '4f2a7da4f872e9807079ac7cb42aefb5'
        record_status = ''
        date_deleted = timezone.now()

        composite_ledger = CompositeLedger(
            unique_record_identifier=unique_record_identifier,
            provider_name=provider_name,
            date_inserted=date_inserted,
            metadata=metadata,
            metadata_hash=metadata_hash,
            metadata_key=metadata_key,
            metadata_key_hash=metadata_key_hash,
            record_status=record_status,
            date_deleted=date_deleted)

        self.assertEqual(composite_ledger.unique_record_identifier,
                         unique_record_identifier)
        self.assertEqual(composite_ledger.provider_name,
                         provider_name)
        self.assertEqual(composite_ledger.date_inserted,
                         date_inserted)
        self.assertEqual(composite_ledger.metadata,
                         metadata)
        self.assertEqual(composite_ledger.metadata_hash,
                         metadata_hash)
        self.assertEqual(composite_ledger.metadata_key,
                         metadata_key)
        self.assertEqual(composite_ledger.metadata_key_hash,
                         metadata_key_hash)
        self.assertEqual(composite_ledger.record_status,
                         record_status)
        self.assertEqual(composite_ledger.date_deleted,
                         date_deleted)
