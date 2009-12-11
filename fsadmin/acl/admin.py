# -*- coding: UTF-8 -*-

from django.contrib import databrowse, admin
from django.utils.translation import ugettext_lazy as _
#from .models import
from fsadmin.acl.models import FSAcl

class FSAclAdmin(admin.ModelAdmin):
    list_display = ('name', 'server', 'enabled',)
    
    save_as = True
    save_on_top = True

admin.site.register(FSAcl, FSAclAdmin)
#databrowse.site.register()
