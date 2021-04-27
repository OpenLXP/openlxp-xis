from django.test import TestCase, tag

from core.models import XISConfiguration
from core.utils.xss_client import (
    read_json_data,
    get_target_validation_schema,
    get_required_recommended_fields_for_validation)


@tag('integration')
class Command(TestCase):
    """Test cases for utils.py function """

    def test_get_target_validation_schema(self):
        """Test to retrieve source validation schema from XIS configuration """
        xisConfig = XISConfiguration(target_schema='p2881_schema.json')
        xisConfig.save()

        result_dict = get_target_validation_schema()
        expected_dict = read_json_data('p2881_schema.json')
        self.assertEqual(expected_dict, result_dict)

    def test_get_required_recommended_fields_for_validation(self):
        """Test for Creating list of fields which are Required and
        recommended """

        xisConfig = XISConfiguration(target_schema='p2881_schema.json')
        xisConfig.save()

        req_dict1, rcm_dict2 = \
            get_required_recommended_fields_for_validation()
        self.assertTrue(req_dict1)
        self.assertTrue(rcm_dict2)
