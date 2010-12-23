# -*- mode: python; coding: utf-8; -*-

from django import forms
from django.contrib import databrowse, admin
#from batchadmin.admin import BatchModelAdmin
from django.utils.translation import ugettext_lazy as _
from fsa.lcr.models import Lcr
import logging

l = logging.getLogger('fsa.lcr.admin')

class LcrLoadForm(forms.ModelForm):
    class Meta:
        model = Lcr

    #title = forms.CharField(label=_(u'ID3 title'), max_length=128, required=False)
    file = forms.FileField(label=_(u'File'), required=True)

    def clean_fieldname(self):

        return self.cleaned_data['name']

    def clean(self):

        return self.cleaned_data

    def save(self):
    #    super(LcrLoadForm, self).save(commit=true)
    #    l.debug("add lcr %s" % self.cleaned_data['carrier_id'])
    #    return True
        instances = self.save(commit=False)

        return instances


class LcrAdmin(admin.ModelAdmin):
    #date_hierarchy = ''
    list_display = ('digits', 'operator_type', 'enabled', 'name', 'carrier_id', 'rate', 'vprice', 'quality', 'reliability', 'date_start', 'site')
    list_filter = ('carrier_id', 'enabled', 'date_start', 'site',)
    #list_editable = ('rate', 'quality', 'reliability')
    list_editable = ('quality', 'reliability',)
    search_fields = ('digits','name',)
    change_readonly_fields = ('digits', 'code', 'operator_type', 'enabled', 'name', 'carrier_id', 'rate', 'price', 'price_currency','cid', 'date_start', 'site', 'weeks', 'time_start', 'time_end')
    actions = ['delete_selected', 'make_enable', 'make_disable']

    # fieldsets = ((None, {
    #                 'fields': ('carrier_id', 'enabled', 'file')
    #             }),) 

    # form = LcrLoadForm
    save_as = True
    save_on_top = True
    list_per_page = 50
    #inlines = []

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        l.debug(instances)

    def make_enable(self, request, queryset):
        rows_updated = queryset.update(enabled=True)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as enabled." % message_bit)

    def make_disable(self, request, queryset):
        rows_updated = queryset.update(enabled=False)
        if rows_updated == 1:
            message_bit = _(u"1 story was")
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as disabled." % message_bit)

    make_disable.short_description = _(u"Mark selected stories as disable")
    make_enable.short_description = _(u"Mark selected stories as enable")

admin.site.register(Lcr, LcrAdmin)
