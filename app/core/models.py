from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import uuid
from django.urls import reverse
from django.forms import ValidationError


class XISConfiguration(models.Model):
    """Model for XIA Configuration """

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
=======

# Create your models here.
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
import uuid
from django.urls import reverse
from django.forms import ValidationError

=======
import uuid
from django.urls import reverse
from django.forms import ValidationError

>>>>>>> 96c3f05 (added configuration model; added validation helper functions)

class XISConfiguration(models.Model):
    """Model for XIA Configuration """

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
<<<<<<< HEAD
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
=======
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
