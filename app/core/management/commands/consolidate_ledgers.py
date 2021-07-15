import logging

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import CompositeLedger, MetadataLedger, SupplementalLedger

logger = logging.getLogger('dict_config_logger')


def put_metadata_ledger_into_composite_ledger(data):
    """ Take Metadata_Ledger data to post to Composite_Ledger"""
    for row in data:
        # Attaching supplemental metadata ledger with metadata ledger
        composite_ledger_dict, supplemental_metadata = \
            append_metadata_ledger_with_supplemental_ledger(row)
        # Setting record_status & deleted_date for updated record
        CompositeLedger.objects.filter(
            metadata_key_hash=row['metadata_key_hash'],
            record_status='Active').exclude(
            metadata_hash=row['metadata_hash']).update(
            date_deleted=timezone.now())
        CompositeLedger.objects.filter(
            metadata_key_hash=row['metadata_key_hash'],
            record_status='Active').exclude(
            metadata_hash=row['metadata_hash']).update(
            record_status='Inactive')

        # Retrieving existing records or creating new record to CompositeLedger
        CompositeLedger.objects.get_or_create(
            unique_record_identifier=row['unique_record_identifier'],
            metadata_key=row['metadata_key'],
            metadata_key_hash=row['metadata_key_hash'],
            metadata=composite_ledger_dict,
            metadata_hash=row['metadata_hash'],
            date_inserted=timezone.now(),
            updated_by='System',
            record_status='Active',
            provider_name=row['provider_name'])
        # Updating existing transmission status in Metadata Ledger
        MetadataLedger.objects.filter(
            unique_record_identifier=row['unique_record_identifier']).update(
            composite_ledger_transmission_status='Successful',
            composite_ledger_transmission_date=timezone.now())

        # Updating existing transmission status in Supplemental Ledger
        SupplementalLedger.objects.filter(
            unique_record_identifier=supplemental_metadata[
                'unique_record_identifier']).update(
            composite_ledger_transmission_status='Successful',
            composite_ledger_transmission_date=timezone.now())

    check_metadata_ledger_transmission_ready_record()


def append_metadata_ledger_with_supplemental_ledger(row):
    """ Get supplemental metadata and further consolidate it with
    metadata ledger"""
    supplemental_metadata = SupplementalLedger.objects.filter(
        metadata_key=row['metadata_key'],
        metadata_key_hash=row['metadata_key_hash'],
        record_status='Active').values('metadata',
                                       'unique_record_identifier').first()

    # Consolidating Metadata Ledger with Supplement Ledger
    composite_ledger_dict = {"Metadata_Ledger": row['metadata'],
                             "Supplemental_Ledger": supplemental_metadata[
                                 'metadata']}

    return composite_ledger_dict, supplemental_metadata


def check_metadata_ledger_transmission_ready_record():
    """Retrieve number of Metadata_Ledger transmission ready records in XIS to
    load into Composite_Ledger """

    data = MetadataLedger.objects.filter(
        metadata_validation_status='Y',
        record_status='Active',
        composite_ledger_transmission_status='Ready').values(
        'unique_record_identifier',
        'metadata_key',
        'metadata_key_hash',
        'metadata_hash',
        'metadata',
        'provider_name')
    # Checking available no. of records to transmit in XIS Metadata Ledger
    if len(data) == 0:
        logger.info("Metadata_Ledger data loading in XIS composite ledger is "
                    "complete")
    else:
        put_metadata_ledger_into_composite_ledger(data)


class Command(BaseCommand):
    """Django command to consolidate the XIS data into XIS Composite_Ledger"""

    def handle(self, *args, **options):
        """ Consolidate the XIS metadata into XIS Composite_Ledger"""
        check_metadata_ledger_transmission_ready_record()
