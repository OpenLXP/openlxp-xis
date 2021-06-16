import logging
from unittest.mock import patch

from ddt import ddt
from django.test import tag

from core.management.commands.load_index_agents import (
    check_records_to_load_into_xse, post_data_to_xse)
from core.management.commands.merge_metadata_in_composite_ledger import (
    check_metadata_ledger_transmission_ready_record,
    put_metadata_ledger_into_composite_ledger)
from core.models import CompositeLedger, MetadataLedger

from .test_setup import TestSetUp

logger = logging.getLogger('dict_config_logger')


@tag('integration')
@ddt
class CommandIntegration(TestSetUp):
    """Test cases for merge_metadata_in_composite_ledger """
    meta_value = {"metadata": {
        "Course": {
            "CourseCode": "apr_06_a03_bs_enus",
            "CourseType": "",
            "CourseTitle": "Appium Concepts with Mac OS X",
            "CourseAudience": "Users who need to enter GF ",
            "DepartmentName": "DSS/CDSE",
            "CourseDescription": "course description",
            "CourseProviderName": "DAU",
            "EducationalContext": "",
            "CourseSectionDeliveryMode": "JKO"
        },
        "CourseInstance": {
            "CourseURL": "https://example@data"
        },
        "General_Information": {
            "EndDate": "end_date",
            "StartDate": "start_date"
        }
    }}

    changed_meta_value = {"metadata": {
        "Course": {
            "CourseCode": "apr_06_a03_bs_enus",
            "CourseType": "",
            "CourseTitle": "Appium Concepts with Mac OS X",
            "CourseAudience": "Users who need to enter GF ",
            "DepartmentName": "DSS/CDSE",
            "CourseDescription": "course description",
            "CourseProviderName": "DAU",
            "EducationalContext": "",
            "CourseSectionDeliveryMode": "JKO"
        },
        "CourseInstance": {
            "CourseURL": "https://example123@data"
        },
        "General_Information": {
            "EndDate": "end_date",
            "StartDate": "start_date"
        }
    }}

    metadata_ledger = MetadataLedger(
        unique_record_identifier='fe16decc-a982-40b2-bd2b-e8ab98b80a6f',
        metadata=meta_value,
        metadata_hash='205b2df155a2dd4783087af1ad07bca8',
        metadata_key_hash='52c6a7eacac672e03e6a8c60c5fa39c2',
        metadata_key='DAU_oper_24_a02_bs_enus',
        metadata_validation_status='Y',
        record_status='Active',
        composite_ledger_transmission_status='N', provider_name='XYZ')

    composite_ledger = CompositeLedger(
        unique_record_identifier='fe16decc-a982-40b2-bd2b-e8ab98b80a6f',
        metadata=meta_value,
        metadata_key_hash='52c6a7eacac672e03e6a8c60c5fa39c2',
        record_status='Active',
        provider_name='XYZ')

    def test_put_metadata_ledger_into_composite_ledger(self):
        """Test to take Metadata_Ledger data to post to Composite_Ledger """
        self.metadata_ledger.save()
        data = MetadataLedger.objects.filter(
            metadata_validation_status='Y',
            record_status='Active',
            composite_ledger_transmission_status='N').values(
            'unique_record_identifier',
            'metadata_key',
            'metadata_key_hash',
            'metadata_hash',
            'metadata',
            'provider_name')
        put_metadata_ledger_into_composite_ledger(data)

        result_query_composite_ledger = CompositeLedger.objects.values(
            'metadata_key',
            'metadata_key_hash',
            'metadata_hash',
            'metadata',
            'date_inserted',
            'updated_by',
            'record_status',
            'provider_name').filter(
            unique_record_identifier=self.unique_record_identifier).first()

        result_query_metadata_ledger = MetadataLedger.objects.values(
            'composite_ledger_transmission_status',
            'composite_ledger_transmission_date').filter(
            unique_record_identifier=self.unique_record_identifier).first()

        self.assertTrue(result_query_metadata_ledger.get(
            'composite_ledger_transmission_status'))
        self.assertTrue(result_query_metadata_ledger.get(
            'composite_ledger_transmission_date'))
        self.assertEquals(data[0].get('metadata_key'),
                          result_query_composite_ledger['metadata_key'])
        self.assertEquals(data[0].get('metadata_key_hash'),
                          result_query_composite_ledger.get(
                              'metadata_key_hash'))
        self.assertEquals(data[0].get('metadata_hash'),
                          result_query_composite_ledger.get('metadata_hash'))
        self.assertTrue(result_query_composite_ledger.get('date_inserted'))
        self.assertEquals(self.updated_by,
                          result_query_composite_ledger.get('updated_by'))
        self.assertEquals(data[0].get('provider_name'),
                          result_query_composite_ledger.get('provider_name'))

    @patch('core.management.commands.merge_metadata_in_composite_ledger'
           '.put_metadata_ledger_into_composite_ledger', return_value=None)
    def test_check_metadata_ledger_transmission_ready_record_one_record(
            self, mock_put_metadata_ledger_into_composite_ledger):
        """Test to retrieve number of Metadata_Ledger transmission ready
        records in XIS to load into Composite_Ledger """
        self.metadata_ledger.save()
        check_metadata_ledger_transmission_ready_record()
        self.assertEqual(
            mock_put_metadata_ledger_into_composite_ledger.call_count, 1)

    @patch('core.management.commands.merge_metadata_in_composite_ledger'
           '.put_metadata_ledger_into_composite_ledger', return_value=None)
    def test_check_metadata_ledger_transmission_ready_record_zero_record(
            self, mock_put_metadata_ledger_into_composite_ledger):
        """Test to retrieve number of Metadata_Ledger transmission ready
        records in XIS to load into Composite_Ledger """
        check_metadata_ledger_transmission_ready_record()
        self.assertEqual(
            mock_put_metadata_ledger_into_composite_ledger.call_count, 0)

    """Test cases for load_index_agents """

    def test_post_data_to_xse_created(self):
        """Test for POSTing XIS composite_ledger to XSE in JSON format when
            record gets created in XSE"""

        self.composite_ledger.save()

        data = CompositeLedger.objects.filter(
            record_status='Active',
            metadata_transmission_status='Ready').values(
            'metadata_key_hash',
            'metadata')
        with patch('elasticsearch.Elasticsearch.index') as response_obj:
            response_obj.return_value = {
                "result": "created"
            }

            post_data_to_xse(data)

            result_query = CompositeLedger.objects.values(
                'metadata_transmission_status_code',
                'metadata_transmission_status',
                'date_transmitted').filter(
                metadata_key_hash=self.metadata_key_hash).first()

            self.assertEqual('created', result_query.get(
                'metadata_transmission_status_code'))
            self.assertEqual('Successful', result_query.get(
                'metadata_transmission_status'))
            self.assertTrue(result_query.get(
                'date_transmitted'))

    def test_post_data_to_xse_updated(self):
        """Test for POSTing XIS composite_ledger to XSE in JSON format when
            record gets updated in XSE"""
        self.composite_ledger.save()
        composite_ledger = CompositeLedger(
            unique_record_identifier='fe16decc-a982-40b2-bd2b-e8ab98b80a6f',
            metadata=self.changed_meta_value,
            metadata_key_hash='52c6a7eacac672e03e6a8c60c5fa39c2',
            record_status='Active',
            provider_name='XYZ')
        composite_ledger.save()

        data = CompositeLedger.objects.filter(
            record_status='Active',
            metadata_transmission_status='Ready').values(
            'metadata_key_hash',
            'metadata')
        with patch('elasticsearch.Elasticsearch.index') as response_obj:
            response_obj.return_value = {
                "result": "updated"
            }

            post_data_to_xse(data)

            result_query = CompositeLedger.objects.values(
                'metadata_transmission_status_code',
                'metadata_transmission_status',
                'date_transmitted').filter(
                metadata_key_hash=self.metadata_key_hash).first()

            self.assertEqual('updated', result_query.get(
                'metadata_transmission_status_code'))
            self.assertEqual('Successful', result_query.get(
                'metadata_transmission_status'))
            self.assertTrue(result_query.get(
                'date_transmitted'))

    def test_post_data_to_xse_failed(self):
        """Test for POSTing XIS composite_ledger to XSE in JSON format when
            request fails"""
        self.composite_ledger.save()
        data = CompositeLedger.objects.filter(
            record_status='Active',
            metadata_transmission_status='Ready').values(
            'metadata_key_hash',
            'metadata')
        with patch('elasticsearch.Elasticsearch.index') as response_obj:
            response_obj.return_value = {
                "result": "failed"
            }

            post_data_to_xse(data)

            result_query = CompositeLedger.objects.values(
                'metadata_transmission_status_code',
                'metadata_transmission_status',
                'date_transmitted').filter(
                metadata_key_hash=self.metadata_key_hash).first()

            self.assertEqual('failed', result_query.get(
                'metadata_transmission_status_code'))
            self.assertEqual('Failed', result_query.get(
                'metadata_transmission_status'))
            self.assertTrue(result_query.get(
                'date_transmitted'))

    @patch('core.management.commands.load_index_agents'
           '.post_data_to_xse', return_value=None)
    def test_check_records_to_load_into_xse_one_record(self,
                                                       mock_post_data_to_xse):
        """Test to retrieve number of Composite_Ledger records in XIS to load
         into XSE and calls the post_data_to_xis accordingly"""
        self.composite_ledger.save()
        check_records_to_load_into_xse()
        self.assertEqual(
            mock_post_data_to_xse.call_count, 1)

    @patch('core.management.commands.load_index_agents'
           '.post_data_to_xse', return_value=None)
    def test_check_records_to_load_into_xse_zero_record(self,
                                                        mock_post_data_to_xse):
        """Test to retrieve number of Composite_Ledger records in XIS to load
        into XSE and calls the post_data_to_xis accordingly"""
        check_records_to_load_into_xse()
        self.assertEqual(
            mock_post_data_to_xse.call_count, 0)
