import logging
import os

logger = logging.getLogger('dict_config_logger')


def get_elasticsearch_endpoint():
    """Setting API endpoint for XIS and XSE  communication """
    api_es_endpoint = os.environ.get('ES_ENDPOINT')
    return api_es_endpoint


def get_elasticsearch_index():
    """Setting elastic search index """
    api_es_index = os.environ.get('ES_INDEX')
    return api_es_index
