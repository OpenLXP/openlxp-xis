import json
from unittest.mock import patch

from ddt import data, ddt
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


@tag('unit')
@ddt
class ViewTests(APITestCase):

    def test_get_records_provider_not_found(self):
        """Test that the /api/metadata/ endpoint returns the correct error
            if no provider name is found"""
        url = "%s?provider=test" % (reverse('api:metadata'))

        with patch('api.views.CompositeLedger.objects') as compositeObj:
            compositeObj.return_value = compositeObj
            compositeObj.filter.side_effect = [compositeObj, None]
            compositeObj.all.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj

            response = self.client.get(url)
            responseDict = json.loads(response.content)
            expected_error = "Error; no provider name found for: test"

            self.assertEqual(response.status_code,
                             status.HTTP_400_BAD_REQUEST)
            self.assertEqual(responseDict['message'], expected_error)

    def test_get_records_provider_found(self):
        """Test that the /api/metadata/ endpoint returns an object
           if provider name is found"""
        url = "%s?provider=test" % (reverse('api:metadata'))
        result_obj = {
            "test": "test"
        }

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer') as serializer:
            compositeObj.return_value = compositeObj
            compositeObj.filter.side_effect = [compositeObj, result_obj]
            compositeObj.all.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            serializer.return_value = serializer
            serializer.data = result_obj

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)
            self.assertEqual(responseDict, result_obj)

    def test_get_records_id_not_found(self):
        """Test that the /api/metadata/ endpoint returns the correct error
            if no id is found"""
        url = "%s?id=test" % (reverse('api:metadata'))

        with patch('api.views.CompositeLedger.objects') as compositeObj:
            compositeObj.return_value = compositeObj
            compositeObj.filter.side_effect = [compositeObj, None]
            compositeObj.all.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj

            response = self.client.get(url)
            responseDict = json.loads(response.content)
            expected_error = ("Error; no unique record identidier found for: "
                              "test")

            self.assertEqual(response.status_code,
                             status.HTTP_400_BAD_REQUEST)
            self.assertEqual(responseDict['message'], expected_error)

    @data("1", "1,12", "12345,4232,1313,")
    def test_get_records_id_found(self, param):
        """Test that the /api/metadata/ endpoint returns an object
           if the id(s) are found"""
        url = "%s?id=%s" % (reverse('api:metadata'), param)
        result_obj = {
            "test": "test"
        }

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer') as serializer:
            compositeObj.return_value = compositeObj
            compositeObj.filter.side_effect = [compositeObj, result_obj]
            compositeObj.all.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            serializer.return_value = serializer
            serializer.data = result_obj

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)
            self.assertEqual(responseDict, result_obj)

    def test_get_records_no_param(self):
        """Test that the /api/metadata/ endpoint returns a list of records
           if no parameter is sent"""
        url = reverse('api:metadata')
        result_obj = {
            "test": "test"
        }

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer') as serializer:
            compositeObj.return_value = compositeObj
            compositeObj.filter.side_effect = [compositeObj, result_obj]
            compositeObj.all.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            serializer.return_value = serializer
            serializer.data = result_obj

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)
            self.assertEqual(responseDict, result_obj)
