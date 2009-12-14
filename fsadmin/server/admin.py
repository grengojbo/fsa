# -*- coding: UTF-8 -*-

from django.contrib import databrowse, admin
from django.utils.translation import ugettext_lazy as _
from fsa.server.models import Server, SipProfile, Alias, Conf
from django.contrib.auth.models import User
from django.conf import settings

class ServerAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'listen_ip', 'listen_port', 'enabled')
    #search_fields = ('name', 'text')
    #list_filter = ('date', 'is_draft', 'site')
    fieldsets = (
        (None, {'fields': ('name', 'password', ('listen_ip', 'listen_port'), 'enabled')}),
        (_(u'UnixODBC'), {
            'classes': ('collapse',),
            'fields': ('sql_name', 'sql_login', 'sql_password')}),
        (_(u'SSH params'), {
            'classes': ('collapse',),
            'fields': ('ssh_user', 'ssh_password', 'ssh_host')}),
        )

class ConfAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled')

class SipProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'server', 'domain', 'sip_ip', 'sip_port', 'enabled')

databrowse.site.register(Server)
databrowse.site.register(SipProfile)

admin.site.register(Server, ServerAdmin)
admin.site.register(SipProfile, SipProfileAdmin)
admin.site.register(Alias)
admin.site.register(Conf, ConfAdmin)
