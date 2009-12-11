# -*- coding: UTF-8 -*-

from django.contrib import admin
#from batchadmin.admin import BatchModelAdmin
from django.utils.translation import ugettext_lazy as _
from fsadmin.numberplan.models import NumberPlan

def make_enable(modeladmin, request, queryset):
    rows_updated = queryset.update(enable=True)
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    #self.message_user(request, "%s successfully marked as enabled." % message_bit)
    make_enable.short_description = "Mark selected stories as enable"

class NumberPlanAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'nt', 'enables',)
    list_filter = ('nt', 'enables')
    search_fields = ('phone_number',)
    actions = ['delete_selected', make_enable, 'make_disable']
    
    def make_disable(self, request, queryset):
        rows_updated = queryset.update(enable=False)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as disabled." % message_bit)
    
    make_disable.short_description = _(u"Mark selected stories as disable")
    
    save_as = True
    save_on_top = True
    list_per_page = 50

admin.site.register(NumberPlan, NumberPlanAdmin)

