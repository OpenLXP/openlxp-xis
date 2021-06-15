import logging
from unittest.mock import patch

from django.test import tag

from .test_setup import TestSetUp

logger = logging.getLogger('dict_config_logger')


@tag('unit')
class TestViews(TestSetUp):
    """Class with tests related to Views"""

    def test_post_success_with_data(self):
        """Test to check if views are accepting api and responding
                       accurately if there is data sent """
        res = self.client.post(self.metadata_url,
                               self.metadataLedger_data_valid,
                               format="json")
        with patch(
                'api.views.MetadataLedgerSerializer.is_valid',
                return_value=True), patch('api.views'
                                          '.MetadataLedgerSerializer.save',
                                          return_value=res.data), \
                patch('api.views.MetadataLedgerSerializer.data',
                      return_value=res.data):
            self.assertEqual(res.status_code, 201)
            self.assertEqual(res.data,
                             self.
                             metadataLedger_data_valid[
                                 'unique_record_identifier'])
