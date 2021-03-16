import logging
from django.utils import timezone
from django.core.management.base import BaseCommand
from core.models import MetadataLedger, CompositeLedger

logger = logging.getLogger('dict_config_logger')


def put_metadata_ledger_into_composite_ledger(data):
    """ Take Metadata_Ledger data to post to Composite_Ledger"""

    # Setting record_status & deleted_date for updated record
    CompositeLedger.objects.filter(
        metadata_key_hash=data['metadata_key_hash'],
        record_status='Active').exclude(
        metadata_hash=data['metadata_hash']).update(
        date_deleted=timezone.now())
    CompositeLedger.objects.filter(
        metadata_key_hash=data['metadata_key_hash'],
        record_status='Active').exclude(
        metadata_hash=data['metadata_hash']).update(
        record_status='Inactive')

    # Retrieving existing records or creating new record to CompositeLedger
    CompositeLedger.objects.get_or_create(unique_record_identifier=
                                          data['unique_record_identifier'],
                                          metadata_key=data['metadata_key'],
                                          metadata_key_hash=
                                          data['metadata_key_hash'],
                                          metadata=
                                          data['metadata'],
                                          metadata_hash=
                                          data['metadata_hash'],
                                          date_inserted=timezone.now(),
                                          updated_by='System',
                                          record_status='Active')
    # Updating existing records or creating new record to CompositeLedger
    MetadataLedger.objects.filter(unique_record_identifier=
                                  data['unique_record_identifier']).update(
        composite_ledger_transmission_status='Y',
        composite_ledger_transmission_date=timezone.now())

    return


def check_metadata_ledger_transmission_ready_record():
    """Retrieve number of Metadata_Ledger transmission ready records in XIS to
    load into Composite_Ledger """

    data = MetadataLedger.objects.filter(
        metadata_validation_status='Y',
        record_status='Active',
        composite_ledger_transmission_status='N').all()

    # Checking available no. of records to transmit in XIS Metadata Ledger
    if len(data) == 0:
        logger.info("Metadata_Ledger data loading in XIS composite ledger is "
                    "complete")
    else:
        # Get record to load from XIS metadata_ledger
        data = MetadataLedger.objects.filter(
            record_status='Active',
            metadata_validation_status='Y',
            composite_ledger_transmission_status='N').values(
            'unique_record_identifier',
            'metadata_key',
            'metadata_key_hash',
            'metadata_hash',
            'metadata').first()
        put_metadata_ledger_into_composite_ledger(data)
        check_metadata_ledger_transmission_ready_record()


class Command(BaseCommand):
    """Django command to merge the XIS data into XIS Composite_Ledger"""

    def handle(self, *args, **options):
        """ Merge the XIS metadata into XIS Composite_Ledger"""
        check_metadata_ledger_transmission_ready_record()
