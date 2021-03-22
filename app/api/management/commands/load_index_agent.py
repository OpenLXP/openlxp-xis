import logging
from django.core.serializers.json import DjangoJSONEncoder
import requests
from django.core.management.base import BaseCommand
from core.models import CompositeLedger, MetadataLedger
import json
from django.utils import timezone
from elasticsearch import Elasticsearch

from api.management.utils.xse_client import get_elasticsearch_endpoint, \
    get_elasticsearch_index

es = Elasticsearch()

logger = logging.getLogger('dict_config_logger')


def renaming_xia_for_posting_to_xis(data):
    """Renaming XIS column names to match with XSE"""

    data['_id'] = data.pop('metadata_key_hash')
    data['metadata'] = data.pop('metadata')
    return data


def post_data_to_xse(data):
    """POSTing XIS composite_ledger to XSE in JSON format"""
    # Traversing through each row one by one from data
    for row in data:
        data = renaming_xia_for_posting_to_xis(row)
        renamed_data = json.dumps(data['metadata'], cls=DjangoJSONEncoder)
        # Getting UUID to update metadata_transmission_status to pending
        metadata_key_hash_val = data.get('_id')

        # Updating status in XIS Composite_Ledger to 'Pending'
        CompositeLedger.objects.filter(
            metadata_key_hash=metadata_key_hash_val).update(
            metadata_transmission_status='Pending')
        # POSTing Composite_Ledger to XSE
        try:
            es = Elasticsearch(get_elasticsearch_endpoint())
            res = es.index(index=get_elasticsearch_index(), doc_type="_doc",
                           id=data['_id'],
                           body=renamed_data)

            # Receiving XSE response after validation and updating
            # Composite_Ledger
            if res['result'] == "created":
                CompositeLedger.objects.filter(
                    metadata_key_hash=metadata_key_hash_val).update(
                    metadata_transmission_status_code=
                    res['result'],
                    metadata_transmission_status='Successful',
                    date_transmitted=timezone.now())
            else:
                CompositeLedger.objects.filter(
                    metadata_key_hash=metadata_key_hash_val).update(
                    metadata_transmission_status_code=
                    res['result'],
                    metadata_transmission_status='Failed',
                    date_transmitted=timezone.now())
                logger.warning("Bad request sent " + str(res['result'])
                               + "error found ")

        except requests.exceptions.RequestException as e:
            logger.error(e)
            raise SystemExit('Exiting! Can not make connection with XSE.')
    check_records_to_load_into_xse()


def check_records_to_load_into_xse():
    """Retrieve number of Composite_Ledger records in XIS to load into XSE and
    calls the post_data_to_xis accordingly"""

    data = CompositeLedger.objects.filter(
        record_status='Active',
        metadata_transmission_status='Ready').values(
        'metadata_key_hash',
        'metadata')

    # Checking available no. of records in XIA to load into XIS is Zero or not
    if len(data) == 0:
        logger.info("Data Loading in XSE is complete, Zero records are "
                    "available in XIS to transmit")
    else:
        post_data_to_xse(data)


class Command(BaseCommand):
    """Django command to load Composite_Ledger in the Experience Search Engine
        (XSE)"""

    def handle(self, *args, **options):
        """Metadata load from XIS Composite_Ledger to XSE"""

        check_records_to_load_into_xse()
