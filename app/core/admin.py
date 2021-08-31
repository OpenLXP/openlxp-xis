from django.contrib import admin

from core.models import XISConfiguration


# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('target_schema', 'xse_host', 'xse_index',)
    fields = [('target_schema', 'xse_host', 'xse_index',)]
