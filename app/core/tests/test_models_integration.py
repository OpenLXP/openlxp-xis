from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from core.models import XISConfiguration


@tag('integration')
class ModelTests(TestCase):

    def test_create_two_xis_configuration(self):
        """Test that trying to create more than one XIS Configuration throws
        ValidationError """
        with self.assertRaises(ValidationError):
            xisConfig = XISConfiguration(target_schema="example1.json")
            xisConfig2 = XISConfiguration(target_schema="example2.json")
            xisConfig.save()
            xisConfig2.save()
