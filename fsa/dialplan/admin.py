# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fsa.dialplan.models import Context, Extension

class ContextAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_context',)
    #list_filter = ()
    #search_fields = []
    actions = ['delete_selected']

    #fieldsets = ()
    
    save_as = True
    save_on_top = True
    list_per_page = 50

class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('name', 'dest_num', 'priority_position', 'is_condition', 'continue_on', 'is_temporary', 'enabled', 'desc',)
    list_filter = ('dest_num', 'is_temporary', 'enabled',)
    fieldsets = (
                (None, {
                    'fields': ('name', 'dest_num', 'desc', ('continue_on', 'is_condition', 'enabled', 'is_temporary'), 'priority_position',  'actions_xml',),
                }),
    )
    order = 4
    save_as = True
    save_on_top = True
    list_per_page = 50

admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Context, ContextAdmin)


