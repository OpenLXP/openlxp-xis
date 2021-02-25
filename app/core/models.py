from django.db import models
import uuid
from django.urls import reverse
from django.forms import ValidationError


class XISConfiguration(models.Model):
    """Model for XIS Configuration """

    source_target_mapping = models.CharField(
        default='p2881_target_metadata_schema.json', max_length=200,
        help_text='Enter the schema '
                  'file to map '
                  'target.')
    target_metadata_schema = models.CharField(
        default='p2881_target_validation_schema.json', max_length=200,
        help_text='Enter the target '
                  'schema file to '
                  'validate from.')

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('Configuration-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk and XISConfiguration.objects.exists():
            raise ValidationError('XISConfiguration model already exists')
        return super(XISConfiguration, self).save(*args, **kwargs)