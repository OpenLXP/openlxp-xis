from unittest.mock import patch

from ddt import ddt
from django.test import tag


from api.serializers import MetadataLedgerSerializer

from .test_setup import TestSetUp


@tag('unit')
@ddt
class SerializerTests(TestSetUp):

    def test_MetadataLedgerSerializer_validate(self):
        """Test to check validation in metadata serializer"""
        with patch('core.utils.xss_client'
                   '.get_required_recommended_fields_for_validation') as \
                mock_validate_list, \
                patch('core.utils.xss_client.get_target_validation_schema',
                      return_value=self.target_data_dict), \
                patch('core.utils.xss_client.read_json_data',
                      return_value=None):
            mock_validate_list.return_value = self.required_dict, \
                                              self.recommended_dict
            return_obj = MetadataLedgerSerializer.\
                validate(self, self.metadataLedger_data_valid)
            self.assertTrue(return_obj.get('metadata_validation_status'))
            self.assertTrue(return_obj.get('record_status'))
            self.assertTrue(return_obj.get('date_validated'))
