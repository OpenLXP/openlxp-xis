from django.contrib import admin

from core.models import XISConfiguration, XISSyndication


# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('target_schema', 'xse_host', 'xse_index',)
    fields = [('target_schema', 'xse_host', 'xse_index',)]


@admin.register(XISSyndication)
class XISSyndicationAdmin(admin.ModelAdmin):
    list_display = ('xis_api_endpoint', 'xis_api_endpoint_status')
    fields = [('xis_api_endpoint', 'xis_api_endpoint_status')]
