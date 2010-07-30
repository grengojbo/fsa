# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from fsa.cdr.models import Cdr

admin.site.disable_action('delete_selected')

class CdrAdmin(admin.ModelAdmin):
    list_display = ('accountcode', 'caller_id_number', 'destination_number', 'billsec', 'cash',
                    'start_timestamp', 'hangup_cause', 'direction', 'lcr_rate', 'nibble_rate',)
    list_filter = ('start_timestamp',)
    search_fields = ('accountcode', 'caller_id_number',)

# class CdrConfAdmin(admin.ModelAdmin):
#     save_as = True
#     list_display = ('name', 'server', 'enabled')


admin.site.register(Cdr, CdrAdmin)
#admin.site.register(Conf, CdrConfAdmin)
