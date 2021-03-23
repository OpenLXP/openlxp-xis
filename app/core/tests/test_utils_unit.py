from core.management.utils.xsr_client import aws_get
from django.test import SimpleTestCase, tag


@tag('unit')
class UtilsTests(SimpleTestCase):

    def test_aws_get(self):
        """This will test that the bucket name returned is correct"""
        bucket_name = 'example'
        result_bucket_name = aws_get()

        self.assertEqual(bucket_name, result_bucket_name)
