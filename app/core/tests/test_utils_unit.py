from django.test import SimpleTestCase, tag

from core.utils.utils import aws_get
from core.utils.xse_client import (get_elasticsearch_endpoint,
                                   get_elasticsearch_index)


@tag('unit')
class UtilsTests(SimpleTestCase):
    """This cases for utils.py"""

    def test_aws_get(self):
        """This test is to check if function returns the bucket name"""
        result_bucket_name = aws_get()

        self.assertTrue(result_bucket_name)

    """This cases for xse_client.py"""

    def test_get_elasticsearch_endpoint(self):
        """This test is to check if function returns the elasticsearch
        endpoint """
        result_api_es_endpoint = get_elasticsearch_endpoint()

        self.assertTrue(result_api_es_endpoint)

    def test_get_elasticsearch_index(self):
        """This test is to check if function returns the elasticsearch index"""
        result_api_es_index = get_elasticsearch_index()

        self.assertTrue(result_api_es_index)
