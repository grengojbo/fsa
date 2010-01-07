# -*- mode: python; coding: utf-8; -*-

from django.contrib import databrowse, admin
#from batchadmin.admin import BatchModelAdmin
from django.utils.translation import ugettext_lazy as _
from fsadmin.directory.models import Endpoint, FSGroup

def make_enable(modeladmin, request, queryset):
    rows_updated = queryset.update(enable=True)
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    #self.message_user(request, "%s successfully marked as enabled." % message_bit)
    make_enable.short_description = "Mark selected stories as enable"


class EndpointAdmin(admin.ModelAdmin):
    list_display = ('uid', 'accountcode', 'phone_type', 'enable', 'is_registered',)
    list_filter = ('enable', 'is_registered')
    #list_editable = ('enable',)
    search_fields = ('uid',)
    actions = ['delete_selected', make_enable, 'make_disable']
    
    def make_disable(self, request, queryset):
        rows_updated = queryset.update(enable=False)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as disabled." % message_bit)
    
    make_disable.short_description = _(u"Mark selected stories as disable")

admin.site.register(Endpoint,EndpointAdmin)
admin.site.register(FSGroup)

