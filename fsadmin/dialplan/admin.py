# -*- coding: UTF-8 -*-

from django.contrib import databrowse, admin
from django.utils.translation import ugettext_lazy as _
from fsadmin.dialplan.models import Context, Extension

class ContextAdmin(admin.ModelAdmin):
    #list_display = ()
    #list_filter = ()
    #search_fields = []
    actions = ['delete_selected']

    #fieldsets = ()
    
    save_as = True
    save_on_top = True
    list_per_page = 50

class ExtensionAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
    
    save_as = True
    save_on_top = True
    list_per_page = 50

admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Context, ContextAdmin)


