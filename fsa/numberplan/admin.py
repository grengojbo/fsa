# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
#from batchadmin.admin import BatchModelAdmin
from django.utils.translation import ugettext_lazy as _
from fsa.numberplan.models import NumberPlan

def make_enable(modeladmin, request, queryset):
    rows_updated = queryset.update(enables=True)
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    #self.message_user(request, "%s successfully marked as enabled." % message_bit)
    make_enable.short_description = "Mark selected stories as enable"

class NumberPlanAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'nt', 'enables', 'status', 'date_active')
    list_filter = ('nt', 'enables')
    search_fields = ('phone_number',)
    actions = ['delete_selected', make_enable, 'make_disable', 'make_default', 'make_silver', 'make_gold']
    
    def make_disable(self, request, queryset):
        rows_updated = queryset.update(enables=False)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as disabled." % message_bit)
    
    make_disable.short_description = _(u"Mark selected stories as disable")
    
    def make_default(self, request, queryset):
        rows_updated = queryset.update(nt=1)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as Default." % message_bit)
    
    make_default.short_description = _(u"Mark selected type as Default")
    
    def make_silver(self, request, queryset):
        rows_updated = queryset.update(nt=2)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as Silver." % message_bit)
    
    make_silver.short_description = _(u"Mark selected type as Silver")
    
    def make_gold(self, request, queryset):
        rows_updated = queryset.update(nt=3)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as Gold." % message_bit)
    
    make_gold.short_description = _(u"Mark selected type as Gold")
    
    fieldsets = (
        (None, {'fields': (('phone_number', 'nt', 'status'), 'enables', 'date_active')}),
    )
    
    save_as = True
    save_on_top = True
    list_per_page = 50

admin.site.register(NumberPlan, NumberPlanAdmin)

