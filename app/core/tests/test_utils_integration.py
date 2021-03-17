from django.test import TestCase
from core.models import XISConfiguration
from core.utils.utils import get_target_validation_schema, read_json_data,\
    get_required_recommended_fields_for_target_validation
from django.test import tag


@tag('integration')
class Command(TestCase):
    """Test cases for utils function """

    def test_get_target_validation_schema(self):
        """Test to retrieve source validation schema from XIS configuration """
        xisConfig = XISConfiguration(target_schema='p2881_schema.json')
        xisConfig.save()

        result_dict = get_target_validation_schema()
        expected_dict = read_json_data('p2881_schema.json')
        self.assertEqual(expected_dict, result_dict)

    def test_get_required_recommended_fields_for_target_validation(self):
        """Test for Creating list of fields which are Required and
        recommended """

        xisConfig = XISConfiguration(target_schema='p2881_schema.json')
        xisConfig.save()

        required_dict = {'Course': ['CourseProviderName', 'DepartmentName',
                                    'CourseCode', 'CourseTitle',
                                    'CourseDescription',
                                    'CourseAudience'],
                         'Lifecycle': ['Provider', 'Maintainer']}
        recommended_dict = {'Course': ['EducationalContext'], 'Lifecycle': []}

        req_dict1, rcm_dict2 = \
            get_required_recommended_fields_for_target_validation()
        self.assertEqual(required_dict, req_dict1)
        self.assertEqual(recommended_dict, rcm_dict2)
