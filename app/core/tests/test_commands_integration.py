import logging

from django.test import TestCase, tag

logger = logging.getLogger('dict_config_logger')


@tag('integration')
class Command(TestCase):
    """Test cases for merge_metadata_in_composite_ledger """

    """Test cases for load_index_agents """
