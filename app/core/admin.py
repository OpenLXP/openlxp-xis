from django.contrib import admin

from core.models import (XISConfiguration, ReceiverEmailConfiguration,
                         SenderEmailConfiguration)


# Register your models here.
@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('target_schema', 'xse_host', 'xse_index',)
    fields = [('target_schema', 'xse_host', 'xse_index',)]


@admin.register(ReceiverEmailConfiguration)
class ReceiverEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('email_address',)


@admin.register(SenderEmailConfiguration)
class SenderEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('sender_email_address',)
