import logging

from core.models import XISConfiguration

logger = logging.getLogger('dict_config_logger')


def get_elasticsearch_endpoint():
    """Setting API endpoint for XIS and XSE  communication """
    configuration = XISConfiguration.objects.first()
    api_es_endpoint = configuration.xse_host
    return api_es_endpoint


def get_elasticsearch_index():
    """Setting elastic search index """
    configuration = XISConfiguration.objects.first()
    api_es_index = configuration.xse_index
    return api_es_index
