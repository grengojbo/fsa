# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
#from .models import
from fsa.acl.models import FSAcl, FSAclNode, AclNetworkList
#from grappelli.admin import GrappelliModelAdmin, GrappelliStackedInline, GrappelliTabularInline

class FSAclNodeInline(admin.TabularInline):
    model = FSAclNode
    extra = 0
    classes = ('collapse-open',)
    allow_add = True

class FSAclAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'enabled', 'acl_type',)
    # fieldsets = (
    #             (None, {
    #                 'fields': ('name', 'acl_default', 'enabled', 'acl_type')
    #             }),
    #         )
    inlines = [FSAclNodeInline]
    save_as = True
    save_on_top = True
    order = 3
class AclNetworkListAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','enabled')
    save_as = True
    save_on_top = True
    order = 2

admin.site.register(AclNetworkList, AclNetworkListAdmin)
admin.site.register(FSAcl, FSAclAdmin)
#databrowse.site.register()
