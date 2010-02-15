# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fsa.server.models import Server, SipProfile, Alias, Conf, CsvBase
from django.contrib.auth.models import User
from django.conf import settings

class ServerAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'server_version', 'listen_ip', 'listen_port', 'enabled',)
    #search_fields = ('name', 'text')
    #list_filter = ('date', 'is_draft', 'site')
    order = 0
    fieldsets = (
        (None, {'fields': ('name', 'password', ('listen_ip', 'listen_port', 'listen_acl'), 'enabled')}),
        (_(u'Server Configuration'), {
            'classes': ('collapse',),
            'fields': ('server_version', 'acl')}),
        (_(u'UnixODBC'), {
            'classes':['collapse-open'],
            'fields': ('sql_name', 'sql_login', 'sql_password')}),
        (_(u'SSH params'), {
            'classes': ['collapse-closed'],
            'fields': ('ssh_user', 'ssh_host')}),
        )

class ConfAdmin(admin.ModelAdmin):
    list_display = ('server', 'name', 'enabled')
    order = 4

class SipProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'server', 'domain', 'sip_ip', 'sip_port', 'enabled', 'default_profile',)
    order = 1
    fieldsets = (
        (None, {'fields': ('name', 'domain', ('server', 'enabled', 'proxy_media'), ('default_profile', 'accept_blind_reg'), 'comments')}),
        (_(u'IP address'), {
            'classes': ('collapse-open',),
            'fields': (('sip_ip', 'rtp_ip', 'sip_port'), 'ext_sip_ip', 'ext_rtp_ip')}),
        (_(u'Other'), {
            'classes':['collapse-closed'],
            'fields': ('context', 'codec_prefs', 'outbound_codec_prefs', ('alias', 'gateway'))}),
        (_(u'XML params'), {
            'classes': ['collapse-closed'],
            'fields': ('other_param', 'no_view_param')}),
        )

class AliasAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias_type',)
    save_as = True
    save_on_top = True
    order = 5
    
class CsvBaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)
    save_as = True
    save_on_top = True
    order = 10
    
admin.site.register(Alias, AliasAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(SipProfile, SipProfileAdmin)
admin.site.register(Conf, ConfAdmin)
admin.site.register(CsvBase, CsvBaseAdmin)
