import logging

from django.test import tag

from .test_setup import TestSetUp

logger = logging.getLogger('dict_config_logger')


@tag('unit')
class TestViews(TestSetUp):
    """Class with tests related to Views"""
    def test_post_failed_no_data(self):
        """Test to check if views are accepting api and responding
        accurately if there is no data sent """

        res = self.client.post(self.metadata_url)
        self.assertEqual(res.status_code, 400)

    def test_post_success_with_data(self):
        """Test to check if views are accepting api and responding
               accurately if there is data sent """

        res = self.client.post(self.metadata_url,
                               self.metadataLedger_data_valid, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data,
                         self.
                         metadataLedger_data_valid['unique_record_identifier'])
