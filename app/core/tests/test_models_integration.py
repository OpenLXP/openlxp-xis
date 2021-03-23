from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from core.models import XISConfiguration


@tag('integration')
class ModelTests(TestCase):

    def test_create_two_xia_configuration(self):
        """Test that trying to create more than one XIS Configuration throws
        ValidationError """
        with self.assertRaises(ValidationError):
            xiaConfig = XISConfiguration(target_schema="example1.json")
            xiaConfig2 = XISConfiguration(target_schema="example2.json")
            xiaConfig.save()
            xiaConfig2.save()
