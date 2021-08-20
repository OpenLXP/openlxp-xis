import json
import logging

import elasticsearch
from django.db.models import Q
import requests
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from elasticsearch import Elasticsearch

from core.management.utils.xse_client import (get_elasticsearch_endpoint,
                                              get_elasticsearch_index)
from core.models import CompositeLedger

es = Elasticsearch()

logger = logging.getLogger('dict_config_logger')


def renaming_xis_for_posting_to_xse(data):
    """Renaming XIS column names to match with XSE"""

    data['_id'] = data.pop('metadata_key_hash')
    data['metadata'] = data.pop('metadata')
    return data


def post_data_to_xse(data):
    """POSTing XIS composite_ledger to XSE in JSON format"""
    # Traversing through each row one by one from data
    for row in data:
        # Creating nested json format for XSE
        composite_ledger = create_xse_json_document(row)

        data = renaming_xis_for_posting_to_xse(row)
        renamed_data = json.dumps(composite_ledger, cls=DjangoJSONEncoder)
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
            if res['result'] == "created" or res['result'] == "updated":
                CompositeLedger.objects.filter(
                    metadata_key_hash=metadata_key_hash_val).update(
                    metadata_transmission_status_code=res['result'],
                    metadata_transmission_status='Successful',
                    date_transmitted=timezone.now())
            else:
                CompositeLedger.objects.filter(
                    metadata_key_hash=metadata_key_hash_val).update(
                    metadata_transmission_status_code=res['result'],
                    metadata_transmission_status='Failed',
                    date_transmitted=timezone.now())
                logger.warning("Bad request sent " + str(res['result'])
                               + "error found ")

        except requests.exceptions.RequestException as e:
            logger.error(e)
            # Updating status in XIS metadata_ledger to 'Failed'
            CompositeLedger.objects.filter(
                metadata_key_hash=metadata_key_hash_val).update(
                metadata_transmission_status='Failed')
            raise SystemExit('Exiting! Can not make connection with XSE.')

        except elasticsearch.exceptions.ConnectionError as e:
            logging.error(e)
            CompositeLedger.objects.filter(
                metadata_key_hash=metadata_key_hash_val).update(
                metadata_transmission_status='Failed')
            raise SystemExit('Exiting! Connection error with elastic search')

    check_records_to_load_into_xse()


def create_xse_json_document(row):
    """ Function to Create nested json for XSE """

    # Removing empty/Null data fields in supplemental data to be sent to XSE
    supplemental_data = {k: v for k, v in row['metadata'][
        'Supplemental_Ledger'].items() if v}

    composite_ledger_dict = {"Supplemental_Ledger": supplemental_data}

    for item in row['metadata']['Metadata_Ledger']:
        # Removing empty/Null data fields in metadata to be sent to XSE
        for item_nested in row['metadata']['Metadata_Ledger'][item]:
            if not row['metadata']['Metadata_Ledger'][item][item_nested]:
                row['metadata']['Metadata_Ledger'][item][item_nested] = None

    composite_ledger_dict.update(row['metadata']['Metadata_Ledger'])

    return composite_ledger_dict


def check_records_to_load_into_xse():
    """Retrieve number of Composite_Ledger records in XIS to load into XSE and
    calls the post_data_to_xis accordingly"""

    combined_query = CompositeLedger.objects.filter(
        Q(metadata_transmission_status='Ready') | Q(
            metadata_transmission_status='Failed'))

    data = combined_query.filter(
        record_status='Active').values(
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
