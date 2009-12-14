# -*- mode: python; coding: utf-8; -*- 
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
#from .models import
from fsa.core.models import VoicemailMsgs, VoicemailPrefs, DbData, SipSubscriptions, SipRegistrations, SipSharedAppearanceDialogs, SipSharedAppearanceSubscriptions, SipDialogs, SipPresence, SipAuthentication, SipAlias, LimitData

class VoicemailMsgsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class VoicemailPrefsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class DbDataAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipSubscriptionsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipRegistrationsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipSharedAppearanceDialogsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipSharedAppearanceSubscriptionsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipDialogsAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipPresenceAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipAuthenticationAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class SipAliasAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

class LimitDataAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
   
    save_as = True
    save_on_top = True
    list_per_page = 50

admin.site.register(LimitData, LimitDataAdmin)
admin.site.register(SipAlias, SipAliasAdmin)
admin.site.register(SipAuthentication, SipAuthenticationAdmin)
admin.site.register(SipPresence, SipPresenceAdmin)
admin.site.register(SipDialogs, SipDialogsAdmin)
admin.site.register(SipSharedAppearanceSubscriptions, SipSharedAppearanceSubscriptionsAdmin)
admin.site.register(SipSharedAppearanceDialogs, SipSharedAppearanceDialogsAdmin)
admin.site.register(SipRegistrations, SipRegistrationsAdmin)
admin.site.register(SipSubscriptions, SipSubscriptionsAdmin)
admin.site.register(DbData, DbDataAdmin)
admin.site.register(VoicemailMsgs, VoicemailMsgsAdmin)
admin.site.register(VoicemailPrefs, VoicemailPrefsAdmin)

