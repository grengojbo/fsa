# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fsa.gateway.models import SofiaGateway

# TODO сделать нормальное отображение шлюзов с просмотром активных шлюзов
class SofiaGatewayAdmin(admin.ModelAdmin):
    #date_hierarchy = ''
    list_display = ('id', 'name', 'username', 'vdescriptions', 'status', 'enabled',)
    #list_filter = ()
    #search_fields = []

    fieldsets = (
                (None, {
                    'fields': ('name', 'descriptions', 'prov_url', ('username', 'password',), ('register','enabled',),'realm',)
                }),
                (_(u'Other Registration'), {
                    'classes': ['collapse-open'],
                    'fields': ('from_user', 'from_domain', 'exten', 'proxy', 'register_proxy',)}),
                (_(u'Other Param'), {
                    'classes': ['collapse-closed'],
                    'fields': (('ping', 'expire_seconds', 'retry_seconds',), ('register_transport', 'caller_id_in_from', 'extension_in_contact',), ('direction', 'acl',),)}),
                (_(u'To Dial Plan'), {
                    'classes': ['collapse-closed'],
                    'fields': ('context', ('max_concurrent', 'in_progress_calls',), 'prefix', 'suffix', 'lcr_format',)}),
            )
    
    save_as = True
    save_on_top = True

admin.site.register(SofiaGateway, SofiaGatewayAdmin)
