import logging
from unittest.mock import patch

from ddt import ddt
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import tag

from core.management.commands.conformance_alerts import send_log_email
from core.management.commands.load_index_agents import (
    check_records_to_load_into_xse, post_data_to_xse,
    renaming_xis_for_posting_to_xse)
from core.management.commands.merge_metadata_in_composite_ledger import (
    check_metadata_ledger_transmission_ready_record,
    put_metadata_ledger_into_composite_ledger)
from core.models import (CompositeLedger, MetadataLedger,
                         ReceiverEmailConfiguration, SenderEmailConfiguration)

from .test_setup import TestSetUp

logger = logging.getLogger('dict_config_logger')


@tag('unit')
@ddt
class CommandTests(TestSetUp):
    """Test cases for waitdb """

    def test_wait_for_db_ready(self):
        """Test that waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = gi
            gi.ensure_connection.return_value = True
            call_command('waitdb')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = gi
            gi.ensure_connection.side_effect = [OperationalError] * 5 + [True]
            call_command('waitdb')
            self.assertEqual(gi.ensure_connection.call_count, 6)

    """Test cases for merge_metadata_in_composite_ledger """

    def test_put_metadata_ledger_into_composite_ledger_zero(self):
        """Test for POSTing XIA metadata_ledger to XIS metadata_ledger
        when data is not present"""
        data = []
        with patch(
                'core.management.commands.merge_metadata_in_composite_ledger'
                '.MetadataLedger.objects') as meta_obj, \
                patch(
                    'core.management.commands.'
                    'merge_metadata_in_composite_ledger.CompositeLedger.'
                    'objects') as composite_obj, \
                patch('core.management.commands.'
                      'merge_metadata_in_composite_ledger'
                      '.check_metadata_ledger_transmission_ready_record',
                      return_value=None) as mock_check_records_to_load:
            composite_obj.return_value = composite_obj
            meta_obj.return_value = meta_obj
            composite_obj.exclude.return_value = composite_obj
            composite_obj.update.return_value = composite_obj
            composite_obj.filter.side_effect = [composite_obj, composite_obj,
                                                composite_obj]

            put_metadata_ledger_into_composite_ledger(data)
            self.assertEqual(mock_check_records_to_load.call_count, 1)

    def test_check_metadata_ledger_transmission_ready_record_one_record(self):
        """Test to Retrieve number of Metadata_Ledger transmission ready
        records in XIS to load into Composite_Ledger"""
        with patch('core.management.commands.'
                   'merge_metadata_in_composite_ledger'
                   '.put_metadata_ledger_into_composite_ledger',
                   return_value=None)as \
                mock_post_data_to_composite_ledger, \
                patch('core.management.commands.'
                      'merge_metadata_in_composite_ledger'
                      '.MetadataLedger.objects') as meta_obj:
            meta_data = MetadataLedger(
                metadata_validation_status='Y',
                record_status='Active',
                composite_ledger_transmission_status='N',
                unique_record_identifier=self.unique_record_identifier,
                metadata_key=self.metadata_key,
                metadata_key_hash=self.metadata_key_hash,
                metadata_hash=self.metadata_hash,
                metadata=self.metadata,
                provider_name=self.provider_name)
            meta_obj.return_value = meta_obj
            meta_obj.exclude.return_value = meta_obj
            meta_obj.values.return_value = [meta_data]
            meta_obj.filter.side_effect = [meta_obj, meta_obj]
            check_metadata_ledger_transmission_ready_record()
            self.assertEqual(
                mock_post_data_to_composite_ledger.call_count, 1)

    def test_check_metadata_ledger_transmission_ready_record_zero(self):
        """Test to Retrieve number of Metadata_Ledger records in XIA to load
        into XIS  and calls the post_data_to_xis accordingly"""
        with patch('core.management.commands.'
                   'merge_metadata_in_composite_ledger'
                   '.put_metadata_ledger_into_composite_ledger',
                   return_value=None)as \
                mock_post_data_to_composite_ledger, \
                patch('core.management.commands.'
                      'merge_metadata_in_composite_ledger.MetadataLedger.'
                      'objects') as meta_obj:
            meta_obj.return_value = meta_obj
            meta_obj.exclude.return_value = meta_obj
            meta_obj.filter.side_effect = [meta_obj, meta_obj]
            check_metadata_ledger_transmission_ready_record()
            self.assertEqual(
                mock_post_data_to_composite_ledger.call_count, 0)

    """Test cases for load_index_agents """

    def test_renaming_xis_for_posting_to_xse(self):
        """Test for Renaming XIS column names to match with XSE"""
        return_data = renaming_xis_for_posting_to_xse(self.xis_data)
        self.assertEquals(self.xse_expected_data['_id'],
                          return_data['_id'])
        self.assertEquals(self.xse_expected_data['metadata'],
                          return_data['metadata'])

    def test_check_records_to_load_into_xse_one_record(self):
        """Test to Retrieve number of Composite_Ledger records in XIS to load
        into XSE and calls the post_data_to_xis accordingly for one record"""
        with patch('core.management.commands.load_index_agents'
                   '.post_data_to_xse', return_value=None)as \
                mock_post_data_to_xse, \
                patch('core.management.commands.load_index_agents'
                      '.CompositeLedger.objects') as composite_obj:
            composite_data = CompositeLedger(
                record_status='Active',
                metadata_transmission_status='Ready',
                metadata_key_hash=self.metadata_key_hash,
                metadata=self.metadata)
            composite_obj.return_value = composite_obj
            composite_obj.exclude.return_value = composite_obj
            composite_obj.values.return_value = [composite_data]
            composite_obj.filter.side_effect = [composite_obj, composite_obj]
            check_records_to_load_into_xse()
            self.assertEqual(
                mock_post_data_to_xse.call_count, 1)

    def test_check_records_to_load_into_xse_zero(self):
        """Test to Retrieve number of Composite_Ledger records in XIS to load
        into XSE and calls the post_data_to_xis accordingly for zero records"""
        with patch('core.management.commands.load_index_agents'
                   '.post_data_to_xse', return_value=None)as \
                mock_post_data_to_xse, \
                patch('core.management.commands.load_index_agents'
                      '.CompositeLedger.objects') as meta_obj:
            meta_obj.return_value = meta_obj
            meta_obj.exclude.return_value = meta_obj
            meta_obj.filter.side_effect = [meta_obj, meta_obj]
            check_records_to_load_into_xse()
            self.assertEqual(
                mock_post_data_to_xse.call_count, 0)

    def test_post_data_to_xse_zero(self):
        """Test POSTing XIS composite_ledger to XSE in JSON format
         data is not present"""
        data = []
        with patch('core.management.commands.load_index_agents'
                   '.renaming_xis_for_posting_to_xse',
                   return_value=self.xse_expected_data), \
                patch('core.management.commands.load_index_agents'
                      '.CompositeLedger.objects') as composite_obj, \
                patch('elasticsearch.Elasticsearch.index') as response_obj, \
                patch('core.management.commands.load_index_agents'
                      '.check_records_to_load_into_xse', return_value=None
                      ) as mock_check_records_to_load_into_xse:
            response_obj.return_value = response_obj
            response_obj.return_value = {
                "result": "created"
            }

            composite_obj.return_value = composite_obj
            composite_obj.exclude.return_value = composite_obj
            composite_obj.update.return_value = composite_obj
            composite_obj.filter.side_effect = [composite_obj, composite_obj,
                                                composite_obj,
                                                composite_obj]

            post_data_to_xse(data)
            self.assertEqual(response_obj.call_count, 0)
            self.assertEqual(mock_check_records_to_load_into_xse.call_count, 1)

    def test_post_data_to_xse_more_than_one(self):
        """Test for POSTing XIS composite_ledger to XSE in JSON format
        when more than one rows are passing"""
        data = [self.xis_data,
                self.xis_data]
        with patch('core.management.commands.load_index_agents'
                   '.renaming_xis_for_posting_to_xse',
                   return_value=self.xse_expected_data), \
                patch('core.management.commands.load_index_agents'
                      '.CompositeLedger.objects') as composite_obj, \
                patch('core.management.commands.load_index_agents'
                      '.Elasticsearch') as es_construct, \
                patch('core.management.commands.load_index_agents'
                      '.check_records_to_load_into_xse', return_value=None
                      ) as mock_check_records_to_load_into_xse:
            es_instance = es_construct.return_value
            es_construct.return_value = es_instance
            es_instance.return_value = es_instance
            es_instance.index.return_value = {
                "result": "created"
            }

            composite_obj.return_value = composite_obj
            composite_obj.exclude.return_value = composite_obj
            composite_obj.update.return_value = composite_obj
            composite_obj.filter.side_effect = [composite_obj, composite_obj,
                                                composite_obj,
                                                composite_obj]

            post_data_to_xse(data)
            self.assertEqual(es_instance.index.call_count, 2)
            self.assertEqual(mock_check_records_to_load_into_xse.call_count, 1)

    # Test cases for conformance_alerts

    def test_send_log_email(self):
        """Test for function to send emails of log file to personas"""
        with patch('core.management.commands.conformance_alerts'
                   '.ReceiverEmailConfiguration') as receive_email_cfg, \
                patch('core.management.commands.conformance_alerts'
                      '.SenderEmailConfiguration') as sender_email_cfg, \
                patch('core.management.commands.conformance_alerts'
                      '.send_notifications', return_value=None
                      ) as mock_send_notification:
            receive_email = ReceiverEmailConfiguration(
                email_address=self.receive_email_list)
            receive_email_cfg.first.return_value = receive_email

            send_email = SenderEmailConfiguration(
                sender_email_address=self.sender_email)
            sender_email_cfg.first.return_value = send_email
            send_log_email()
            self.assertEqual(mock_send_notification.call_count, 1)
