import json
from unittest.mock import patch

from ddt import data, ddt
from django.test import tag
from django.urls import reverse
from requests.exceptions import HTTPError
from rest_framework import status

from .test_setup import TestSetUp


@tag('unit')
@ddt
class ViewTests(TestSetUp):

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
            expected_error = ("Error; no unique record identifier found for: "
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

    def test_record_for_requested_course_id(self):
        """Test that the /api/metadata/ID endpoint returns a single record with
            the matching id"""
        doc_id = '123456'
        url = reverse('api:record_for_requested_course_id', args=(doc_id,))

        with patch('api.views.CompositeLedger.objects') as compositeObj:
            compositeObj.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            compositeObj.get.return_value = self.composite_ledger

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)
            self.assertEqual(responseDict['unique_record_identifier'],
                             str(self.unique_record_identifier))

    def test_patch_record_for_course_id(self):
        """Test that the /api/metadata/ID endpoint updates record with
            the matching id"""
        doc_id = '123456'
        url = reverse('api:record_for_requested_course_id', args=(doc_id,))

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer') as serializer:
            compositeObj.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            compositeObj.get.return_value = self.composite_ledger_valid_data

            serializer.return_value = serializer
            serializer.is_valid.return_value = True
            serializer.save.return_value = serializer
            serializer.data = self.composite_ledger_metadata
            dataJSON = json.dumps(self.composite_ledger_metadata)

            response = self.client.patch(url, json=dataJSON)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)
            self.assertEqual(responseDict,
                             {"message": "Data updated successfully"})

    def test_patch_record_for_course_id_invalid(self):
        """Test that the /api/metadata/ID endpoint does not update invalid
        record with the matching id"""
        doc_id = '123456'
        url = reverse('api:record_for_requested_course_id', args=(doc_id,))

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer') as serializer:
            compositeObj.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            compositeObj.get.return_value = self.composite_ledger_valid_data

            serializer.return_value = serializer
            serializer.is_valid.return_value = False
            serializer.save.return_value = serializer
            serializer.data = self.composite_ledger_metadata_invalid
            dataJSON = json.dumps(self.composite_ledger_metadata_invalid)

            response = self.client.patch(url, json=dataJSON)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(responseDict,
                             {"message": "Data is not valid for update"})

    def test_post_record_valid(self):
        """Test that sending a POST request to the /api/metadata endpoint
            succeeds and returns unique record identifier for the new record"""
        url = reverse('api:metadata')

        with patch('api.views.MetadataLedgerSerializer') as serializer:
            serializer.return_value = serializer
            serializer.is_valid.return_value = True
            serializer.save.return_value = serializer
            serializer.data = self.metadataLedger_data_valid
            dataJSON = json.dumps(self.metadataLedger_data_valid)

            response = self.client.post(url, json=dataJSON)
            responseDict = json.loads(response.content)
            uid = self.metadataLedger_data_valid['unique_record_identifier']

            self.assertEqual(response.status_code,
                             status.HTTP_201_CREATED)
            self.assertEqual(responseDict, uid)

    def test_post_record_invalid(self):
        """Test that sending a POST request to the /api/metadata endpoint
            succeeds and returns unique record identifier for the new record"""
        url = reverse('api:metadata')

        with patch('api.views.MetadataLedgerSerializer') as serializer:
            serializer.return_value = serializer
            serializer.is_valid.return_value = True
            serializer.save.return_value = serializer
            serializer.data = self.metadataLedger_data_invalid
            dataJSON = json.dumps(self.metadataLedger_data_invalid)

            response = self.client.post(url, json=dataJSON)
            responseDict = json.loads(response.content)
            uid = self.metadataLedger_data_invalid['unique_record_identifier']

            self.assertEqual(response.status_code,
                             status.HTTP_201_CREATED)
            self.assertEqual(responseDict, uid)

    def test_post_composite_record_valid(self):
        """Test that sending a POST request to the /api/supplemental-data
        endpoint succeeds and returns unique record identifier for the new
        record"""
        url = reverse('api:supplemental-data')

        with patch('api.views.SupplementalLedgerSerializer') as serializer:
            serializer.return_value = serializer
            serializer.is_valid.return_value = True
            serializer.save.return_value = serializer
            serializer.data = self.supplemental_data
            dataJSON = json.dumps(self.supplemental_data)

            response = self.client.post(url, json=dataJSON)
            responseDict = json.loads(response.content)
            uid = self.supplemental_data['unique_record_identifier']

            self.assertEqual(response.status_code,
                             status.HTTP_201_CREATED)
            self.assertEqual(responseDict, uid)

    def test_patch_record_for_course_id_fail(self):
        """Test that the /api/metadata/ID endpoint returns a 500 error if an
            exception is thrown"""
        doc_id = '123456'
        url = reverse('api:record_for_requested_course_id', args=(doc_id,))

        with patch('api.views.CompositeLedger.objects') as compositeObj, \
                patch('api.views.CompositeLedgerSerializer'):
            compositeObj.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            compositeObj.get.side_effect = HTTPError

            dataJSON = json.dumps(self.composite_ledger_metadata_invalid)

            response = self.client.patch(url, json=dataJSON)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_record_for_requested_course_id_fail(self):
        """Test that the /api/metadata/ID endpoint returns a 500 error if an
            exception is thrown"""
        doc_id = '123456'
        url = reverse('api:record_for_requested_course_id', args=(doc_id,))

        with patch('api.views.CompositeLedger.objects') as compositeObj:
            compositeObj.return_value = compositeObj
            compositeObj.order_by.return_value = compositeObj
            compositeObj.get.side_effect = HTTPError

            response = self.client.get(url)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
