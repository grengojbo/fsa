# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fsa.gateway.models import SofiaGateway

# TODO сделать нормальное отображение шлюзов с просмотром активных шлюзов
class SofiaGatewayAdmin(admin.ModelAdmin):
    #date_hierarchy = ''
    list_display = ('id', 'name', 'username', 'realm', 'prefix_number', 'max_concurrent', 'vdescriptions', 'direction', 'status', 'enabled',)
    #list_filter = ()
    #search_fields = []

    fieldsets = (
                (None, {
                    'fields': ('name', 'descriptions', 'prov_url', ('username', 'password',), ('register','enabled',),'realm',)
                }),
                (_(u'Phone number format'), {
                    'classes': ['collapse-open'],
                    'fields': ('prefix_number', 'pref_international', 'pref_national',)
                }),
                (_(u'Phone number format'), {
                    'classes': ['collapse-close'],
                    'fields': ('money_time', 'money_nds', 'money_period', 'price_currency',)
                }),
                (_(u'Other Registration'), {
                    'classes': ['collapse-open'],
                    'fields': ('from_user', 'from_domain', 'exten', 'proxy', 'register_proxy',)}),
                (_(u'Other Param'), {
                    'classes': ['collapse-open'],
                    'fields': (('ping', 'expire_seconds', 'retry_seconds',), ('codec_string',),('register_transport', 'caller_id_in_from', 'extension_in_contact',), ('direction', 'acl',),)}),
                (_(u'To Dial Plan'), {
                    'classes': ['collapse-open'],
                    'fields': ('context', ('max_concurrent', 'in_progress_calls',), 'prefix', 'suffix',)}),
            )
    
    save_as = True
    save_on_top = True

admin.site.register(SofiaGateway, SofiaGatewayAdmin)
