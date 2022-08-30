import uuid

from django.db import models
from django.forms import ValidationError
from django.urls import reverse


class XISConfiguration(models.Model):
    """Model for XIS Configuration """

    target_schema = models.CharField(
        default='p2881', max_length=200,
        help_text='Enter the target '
                  'schema name or IRI '
                  'to validate with.')
    xss_host = models.CharField(
        help_text='Enter the host url for the XSS (Schema Service) to use.',
        max_length=200
    )
    xse_host = models.CharField(
        help_text='Enter the host url for the XSE (Search Engine) to use.',
        max_length=200
    )
    xse_index = models.CharField(
        help_text='Enter the name of the index for the XSE (Search Engine) \
            to query.',
        max_length=200
    )
    autocomplete_field = models.CharField(
        default='metadata.Metadata_Ledger.Course.CourseTitle', max_length=200,
        help_text='Enter the field to support '
                  'autocomplete on in XSE.')
    filter_field = models.CharField(
        default='provider_name', max_length=200,
        help_text='Enter the field to filter XSE queries by.')

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


class Neo4jConfiguration(models.Model):
    """Model for Neo4j Configuration """

    neo4j_uri = models.CharField(max_length=200,
                                 help_text='Enter the host uri for the Neo4j '
                                           '(Graph Database) to use.')
    neo4j_user = models.CharField(
        help_text='Enter the user ID to connect with Neo4j',
        max_length=200)
    neo4j_pwd = models.CharField(
        help_text='Enter the user ID to connect with Neo4j',
        max_length=200)

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('Configuration-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk and Neo4jConfiguration.objects.exists():
            raise ValidationError('Neo4jConfiguration model already exists')
        return super(Neo4jConfiguration, self).save(*args, **kwargs)


class MetadataLedger(models.Model):
    """Model for MetadataLedger"""

    METADATA_VALIDATION_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    RECORD_TRANSMISSION_STATUS_CHOICES = [('Successful', 'S'), ('Failed', 'F'),
                                          ('Pending', 'P'), ('Ready', 'R'),
                                          ('Cancelled', 'C')]
    composite_ledger_transmission_date = models.DateTimeField(blank=True,
                                                              null=True)
    composite_ledger_transmission_status = \
        models.CharField(max_length=10,
                         blank=True,
                         default='Ready',
                         choices=RECORD_TRANSMISSION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_validated = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True)
    metadata_hash = models.CharField(max_length=200)
    metadata_key = models.CharField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_validation_status = \
        models.CharField(max_length=10, blank=True,
                         choices=METADATA_VALIDATION_CHOICES)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.CharField(max_length=250,
                                                primary_key=True)
    updated_by = models.CharField(max_length=10, blank=True, default='System')


class SupplementalLedger(models.Model):
    """Model for SupplementalLedger"""

    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    RECORD_TRANSMISSION_STATUS_CHOICES = [('Successful', 'S'),
                                          ('Failed', 'F'),
                                          ('Pending', 'P'),
                                          ('Ready', 'R'),
                                          ('Cancelled', 'C')]

    composite_ledger_transmission_date = models.DateTimeField(blank=True,
                                                              null=True)
    composite_ledger_transmission_status = \
        models.CharField(max_length=10,
                         blank=True,
                         default='Ready',
                         choices=RECORD_TRANSMISSION_STATUS_CHOICES)
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(null=True, blank=True)
    metadata_hash = models.TextField(max_length=200)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.CharField(max_length=250,
                                                primary_key=True)
    updated_by = models.CharField(max_length=10, blank=True, default='System')


class CompositeLedger(models.Model):
    """Model for CompositeLedger"""

    RECORD_ACTIVATION_STATUS_CHOICES = [('Active', 'A'), ('Inactive', 'I')]
    RECORD_TRANSMISSION_STATUS_CHOICES = [('Successful', 'S'), ('Failed', 'F'),
                                          ('Pending', 'P'),
                                          ('Ready', 'R'),
                                          ('Cancelled', 'C')]
    date_deleted = models.DateTimeField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    date_transmitted = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True)
    metadata_hash = models.TextField(max_length=200)
    metadata_key = models.TextField(max_length=200)
    metadata_key_hash = models.CharField(max_length=200)
    metadata_transmission_status = \
        models.CharField(max_length=10, blank=True,
                         default='Ready',
                         choices=RECORD_TRANSMISSION_STATUS_CHOICES)
    metadata_transmission_status_code = models.CharField(max_length=200,
                                                         blank=True)
    provider_name = models.CharField(max_length=255, blank=True)
    record_status = models.CharField(max_length=10, blank=True,
                                     choices=RECORD_ACTIVATION_STATUS_CHOICES)
    unique_record_identifier = models.UUIDField(primary_key=True,
                                                default=uuid.uuid4,
                                                editable=False)
    updated_by = models.CharField(max_length=10, blank=True)
    metadata_transmission_status_neo4j = \
        models.CharField(max_length=10, blank=True,
                         default='Ready',
                         choices=RECORD_TRANSMISSION_STATUS_CHOICES)


class FilterRecord(models.Model):
    """Model for Filtering Composite Ledger Experiences for XIS Syndication """
    EQUAL = 'EQUAL'
    UNEQUAL = 'UNEQUAL'
    CONTAINS = 'CONTAINS'

    COMPARATORS = [
        (EQUAL, 'Equal'),
        (UNEQUAL, 'Not Equal'),
        (CONTAINS, 'Contains')]

    field_name = models.CharField(
        help_text='Enter the field path', max_length=255)

    comparator = models.CharField(max_length=200, choices=COMPARATORS)

    field_value = models.CharField(
        help_text='Enter the field value', max_length=255, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return ' '.join([self.field_name, self.comparator, self.field_value])

    def __root_filter(self, queryset):
        """run a query for filtering based on root data"""
        # if using EQUAL, perform a case insensitive exact filter on queryset
        if(self.comparator == self.EQUAL):
            return queryset.filter(
                **{f"{self.field_name}__iexact": self.field_value})
        # if using UNEQUAL, perform a case insensitive exact exclusion
        # on queryset
        elif(self.comparator == self.UNEQUAL):
            return queryset.exclude(
                **{f"{self.field_name}__iexact": self.field_value})
        # if using CONTAINS, perform a case insensitive contains filter
        # on queryset
        elif(self.comparator == self.CONTAINS):
            return queryset.filter(
                **{f"{self.field_name}__icontains": self.field_value})

    def __simple_metadata_filter(self, queryset):
        """run a simple query to filter based on metadata"""
        # if using EQUAL or CONTAINS make a quick query to remove elements
        # that are missing the filter value in metadata
        if(self.comparator == self.EQUAL):
            return queryset.filter(metadata__icontains=self.field_value)
        elif(self.comparator == self.CONTAINS):
            return queryset.filter(metadata__icontains=self.field_value)
        return queryset

    def __metadata_filter(self, queryset):
        """run the more strict query to filter metadata"""
        return_qs = queryset
        # iterate over each item in the queryset
        for exp in queryset:
            # iterate over the fields within metadata to the field
            try:
                path = self.field_name.split('.')[1:]
                metadata = exp.metadata
                for step in path:
                    metadata = metadata[step]
            # if the field does not exist, use an empty string
            except Exception:
                metadata = ''
            # cast metadata field retrieved to a string and exclude items that
            # do not match
            if(self.comparator == self.EQUAL):
                if self.field_value != str(metadata):
                    return_qs = return_qs.exclude(pk=exp.pk)
            elif(self.comparator == self.UNEQUAL):
                if self.field_value == str(metadata):
                    return_qs = return_qs.exclude(pk=exp.pk)
            elif(self.comparator == self.CONTAINS):
                if self.field_value not in str(metadata):
                    return_qs = return_qs.exclude(pk=exp.pk)

        return return_qs

    def apply_filter(self, queryset):
        """Filter the queryset using this filter"""
        if('.' in self.field_name):
            return self.__metadata_filter(
                self.__simple_metadata_filter(queryset))
        else:
            return self.__root_filter(queryset)


class FilterMetadata(models.Model):
    """Model for Filtering Metadata within Composite Ledger Experiences for
    XIS Syndication """
    INCLUDE = 'INCLUDE'
    EXCLUDE = 'EXCLUDE'

    OPERATIONS = [
        (INCLUDE, 'Include'),
        (EXCLUDE, 'Exclude')]

    field_name = models.CharField(
        help_text='Enter the field path', max_length=255)

    operation = models.CharField(max_length=200, choices=OPERATIONS)

    def __str__(self):
        """String for representing the Model object."""
        return ' '.join([self.operation, self.field_name])


class XISUpstream(models.Model):
    """Model for Upstream XIS Syndication """
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')]

    xis_api_endpoint = models.CharField(
        max_length=200,
        help_text='Enter the XIS Instance API endpoint'
    )

    xis_api_endpoint_status = models.CharField(max_length=200, choices=STATUS)

    metadata_experiences = models.ManyToManyField(
        MetadataLedger, related_name='xis_source', blank=True)
    supplemental_experiences = models.ManyToManyField(
        SupplementalLedger, related_name='xis_source', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.xis_api_endpoint}'


class XISDownstream(models.Model):
    """Model for Downstream XIS Syndication """
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')]

    xis_api_endpoint = models.CharField(
        max_length=200,
        help_text='Enter the XIS Instance API endpoint'
    )

    xis_api_endpoint_status = models.CharField(max_length=200, choices=STATUS)

    source_name = models.CharField(
        max_length=200, help_text='Enter the name to send data as')

    composite_experiences = models.ManyToManyField(
        CompositeLedger, related_name='xis_destination', blank=True)

    filter_records = models.ManyToManyField(
        FilterRecord, related_name='xis_downstream', blank=True)
    filter_metadata = models.ManyToManyField(
        FilterMetadata, related_name='xis_downstream', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.xis_api_endpoint}'

    def determine_fields(self):
        """Determines the fields to use from the filter_metadata objects, and
        returns the fields as a tuple of lists include, exclude"""
        exclude = [field.field_name for field in self.filter_metadata.all().
                   filter(operation=FilterMetadata.EXCLUDE)]
        include = [field.field_name for field in self.filter_metadata.all().
                   filter(operation=FilterMetadata.INCLUDE)]
        return include, exclude

    def apply_filter(self, queryset=CompositeLedger.objects.all()):
        """Filter the queryset using this filter"""
        queryset = queryset.filter(
            record_status='Active').exclude(xis_destination__pk=self.pk)
        # iterate FilterRecords to apply filters to queryset
        for record_filter in self.filter_records.all():
            queryset = record_filter.apply_filter(queryset)

        return queryset
