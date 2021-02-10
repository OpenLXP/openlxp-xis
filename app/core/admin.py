from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from core.models import XISConfiguration
=======
from core.models import XISConfiguration

>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)

# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('source_target_mapping', 'target_metadata_schema',)
<<<<<<< HEAD
    fields = [('source_target_mapping', 'target_metadata_schema')]
=======

# Register your models here.
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
    fields = [('source_target_mapping', 'target_metadata_schema')]
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
=======
from core.models import XISConfiguration

# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('source_target_mapping', 'target_metadata_schema',)
    fields = [('source_target_mapping', 'target_metadata_schema')]
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
