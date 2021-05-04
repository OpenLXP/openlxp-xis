import logging

from django.test import tag

from .test_setup import TestSetUp

from core.models import CompositeLedger

from unittest.mock import patch

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

    def test_records_for_provider_name_return_with_no_provider(self):
        """Test to check response for no provider name"""

        res = self.client.get(self.composite_provider_url)
        self.assertEqual(res.status_code, 200)

    def test_records_for_provider_name_return_with_existing_provider(self):
        """Test to check response for existing provider name"""

        with patch(
                'api.views.CompositeLedger.objects') as comp_obj:
            compConfig = CompositeLedger.objects.filter(provider_name='DAU')
            comp_obj.filter.side_effect = compConfig
            comp_obj.exists.return_value = True
            url = "%s?provider=DAU" % (self.composite_provider_url)
            res = self.client.get(url)
            self.assertEqual(res.status_code, 200)

    def test_records_for_provider_name_return_with_nonexistent_provider(self):
        """Test to check response for nonexistent provider name"""

        url = "%s?provider=Test1" % (self.composite_provider_url)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 400)
