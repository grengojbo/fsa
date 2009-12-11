# -*- coding: UTF-8 -*-

from django.contrib import databrowse, admin
#from batchadmin.admin import BatchModelAdmin
from django.utils.translation import ugettext_lazy as _
from fsadmin.cdr.models import Cdr, Conf

admin.site.disable_action('delete_selected')

class CdrAdmin(admin.ModelAdmin):
    list_display = ('accountcode', 'caller_id_number', 'destination_number', 'billsec', 'start_timestamp', 'hangup_cause',)
    list_filter = ('start_timestamp',)
    search_fields = ('accountcode', 'caller_id_number',)

class CdrConfAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('name', 'server', 'enabled')


#databrowse.site.register(Cdr)
#databrowse.site.register(Conf)

admin.site.register(Cdr, CdrAdmin)
admin.site.register(Conf, CdrConfAdmin)
