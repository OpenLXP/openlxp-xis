from uuid import UUID

from django.urls import reverse
from rest_framework.test import APITestCase

from core.models import CompositeLedger, XISConfiguration


class TestSetUp(APITestCase):
    """Class with setup and teardown for tests in XIS"""

    def setUp(self):
        """Function to set up necessary data for testing"""
        self.metadata_url = reverse('api:metadata')
        self.composite_provider_url = reverse('api:metadata')
        self.required_dict = {'Course.CourseProviderName', 'Course.CourseCode',
                              'Course.CourseTitle', 'Course.CourseDescription',
                              'Course.CourseShortDescription',
                              'Course.CourseSubjectMatter',
                              'CourseInstance.CourseCode',
                              'CourseInstance.CourseTitle ',
                              'CourseInstance.StartDate',
                              'CourseInstance.EndDate',
                              'CourseInstance.DeliveryMode',
                              'CourseInstance.Instructor',
                              'General_Information.StartDate',
                              'General_Information.EndDate'}
        self.recommended_dict = {'CourseInstance.Thumbnail',
                                 'Technical_Information.Thumbnail'}

        self.target_data_dict = {
            'Course': {
                'CourseProviderName': 'Required',
                'DepartmentName': 'Optional',
                'CourseCode': 'Required',
                'CourseTitle': 'Required',
                'CourseDescription': 'Required',
                'CourseShortDescription': 'Required',
                'CourseFullDescription': 'Optional',
                'CourseAudience': 'Optional',
                'CourseSectionDeliveryMode': 'Optional',
                'CourseObjective': 'Optional',
                'CoursePrerequisites': 'Optional',
                'EstimatedCompletionTime': 'Optional',
                'CourseSpecialNotes': 'Optional',
                'CourseAdditionalInformation': 'Optional',
                'CourseURL': 'Optional',
                'CourseLevel': 'Optional',
                'CourseSubjectMatter': 'Required'
            },
            'CourseInstance': {
                'CourseCode': 'Required',
                'CourseTitle': 'Required',
                'Thumbnail': 'Recommended',
                'CourseShortDescription': 'Optional',
                'CourseFullDescription': 'Optional',
                'CourseURL': 'Optional',
                'StartDate': 'Required',
                'EndDate': 'Required',
                'EnrollmentStartDate': 'Optional',
                'EnrollmentEndDate': 'Optional',
                'DeliveryMode': 'Required',
                'InLanguage': 'Optional',
                'Instructor': 'Required',
                'Duration': 'Optional',
                'CourseLearningOutcome': 'Optional',
                'CourseLevel': 'Optional',
                'InstructorBio': 'Optional'
            },
            'General_Information': {
                'StartDate': 'Required',
                'EndDate': 'Required'
            },
            'Technical_Information': {
                'Thumbnail': 'Recommended'
            }
        }
        XISConfiguration.objects.create(target_schema='p2881_schema.json',
                                        xse_host='host', xse_index='index')
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

        self.unique_record_identifier = UUID(
            '09edea0e-6c83-40a6-951e-2acee3e99502')
        self.metadata_hash = 'df0b51d7b45ca29682e930d236963584',
        self.metadata_key = 'TestData 123_AGENT',
        self.metadata_key_hash = '6acf7689ea81a1f792e7668a23b1acf5',
        self.provider_name = 'AGENT'
        self.updated_by = 'System'
        self.metadata_1 = {
            "Course": {
                "CourseCode": "TestData 123",
                "CourseTitle": "Acquisition Law",
                "CourseAudience": "test_data",
                "DepartmentName": "",
                "CourseObjective": "test_data",
                "CourseDescription": "test_data",
                "CourseProviderName": "AGENT",
                "CourseSpecialNotes": "test_data",
                "CoursePrerequisites": "None",
                "EstimatedCompletionTime": "4.5 days",
                "CourseSectionDeliveryMode": "Resident",
                "CourseAdditionalInformation": "None"
            },
            "CourseInstance": {
                "CourseURL": "https://url.tes.com123/ui/lms-learning-details"
            },
            "General_Information": {
                "EndDate": "end_date",
                "StartDate": "start_date"
            }
        }

        self.composite_ledger = CompositeLedger(
            unique_record_identifier=self.unique_record_identifier,
            metadata=self.metadata_1,
            metadata_key=self.metadata_key,
            metadata_key_hash=self.metadata_key_hash,
            record_status='Active',
            provider_name='AGENT')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
