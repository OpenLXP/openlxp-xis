from core.models import XISConfiguration
from django.contrib import admin


# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('target_schema',)
