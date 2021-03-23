from django.urls import reverse
from rest_framework.test import APITestCase

from core.models import XISConfiguration


class TestSetUp(APITestCase):
    """Class with setup and teardown for tests in XIS"""

    def setUp(self):
        """Function to set up necessary data for testing"""
        self.metadata_url = reverse('metadata')
        XISConfiguration.objects.create(target_schema='p2881_schema.json')
        self.metadataLedger_data_valid = {
            "provider_name": "DAU",
            "unique_record_identifier": "fe16decc-a982-40b2-bd2b-e8ab98b80a6e",
            "metadata": {
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
            },
            "metadata_hash": "4f2a7da4f872e9807079ac7cb42aefb4",
            "metadata_key": "DAU_apr_06_a03_bs_enus",
            "metadata_key_hash": "4f2a7da4f872e9807079ac7cb42aefb5"
        }

        self.metadataLedger_data_valid_2 = {
            "provider_name": "DAU",
            "unique_record_identifier": "fe16decc-a982-40b2-bd2b-e8ab98b80a6g",
            "metadata": {
                "Course": {
                    "CourseCode": "apr_06_a03_bs_enus",
                    "CourseType": "",
                    "CourseTitle": "Appium Concepts with Mac OS X",
                    "CourseAudience": "Users who need to enter GF ",
                    "DepartmentName": "DSS/CDSE",
                    "CourseDescription": "course description",
                    "CourseProviderName": "DAU1",
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
            },
            "metadata_hash": "4f2a7da4f872e9807079ac7cb42aefb5",
            "metadata_key": "DAU_apr_06_a03_bs_enus",
            "metadata_key_hash": "4f2a7da4f872e9807079ac7cb42aefb5"
        }

        self.metadataLedger_data_invalid = {
            "provider_name": "DAU",
            "unique_record_identifier": "fe16decc-a982-40b2-bd2b-e8ab98b80a6f",
            "metadata": {
                "Course": {
                    "CourseCode": "apr_06_a03_bs_enus",
                    "CourseType": "",
                    "CourseTitle": "Appium Concepts with Mac OS X",
                    "CourseAudience": "Users who need to enter GF ",
                    "DepartmentName": "DSS/CDSE",
                    "CourseDescription": "course description",
                    "CourseProviderName": "",
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
            },
            "metadata_hash": "4f2a7da4f872e9807079ac7cb42aefb6",
            "metadata_key": "DAU_apr_06_a03_bs_enus",
            "metadata_key_hash": "4f2a7da4f872e9807079ac7cb42aefb5"
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
