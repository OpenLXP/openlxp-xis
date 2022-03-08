from django.contrib import admin

from core.models import Neo4jConfiguration, XISConfiguration, XISSyndication


# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('target_schema', 'xse_host', 'xse_index',)
    fields = [('target_schema', 'xse_host', 'xse_index',)]


@admin.register(XISSyndication)
class XISSyndicationAdmin(admin.ModelAdmin):
    list_display = ('xis_api_endpoint', 'xis_api_endpoint_status')
    fields = [('xis_api_endpoint', 'xis_api_endpoint_status')]


@admin.register(Neo4jConfiguration)
class Neo4jConfigurationAdmin(admin.ModelAdmin):
    list_display = ('neo4j_uri', 'neo4j_user', 'neo4j_pwd',)
    fields = [('neo4j_uri', 'neo4j_user', 'neo4j_pwd',)]
