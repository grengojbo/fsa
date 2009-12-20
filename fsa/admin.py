# -*- mode: python; coding: utf-8; -*- 
"""
admin.py

Created by jbo on 2009-12-13.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
from django.contrib import admin
from grappelli.sites import GrappelliSite
from django.utils.translation import ugettext_lazy as _
# 
# from django.contrib.auth.models import User, Group
# from django.contrib.auth.admin import GroupAdmin, UserAdmin
# from django.contrib.sites.models import Site
# from django.contrib.sites.admin import SiteAdmin
# from l10n.models import Country
# from l10n.admin import CountryOptions
# 
user_site = GrappelliSite()
# #user_site.register(UserExtendedProfile, UserExtendedProfileOptions)
# #user_site.register(UserProfile, UserProfileOptions)
# user_site.register(Group, GroupAdmin)
# user_site.register(User, UserAdmin)
# user_site.register(Site, SiteAdmin)
# user_site.register(Country, CountryOptions)

admin.site = GrappelliSite()
admin.autodiscover()

admin.site.groups = {
    0: {
        'title': 'User Management Administration', # optional
        'name': 'User Management',
        'apps': ['auth', 'l10n'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-open'], # optional
        'show_apps': False, # optional
    },
    1: {
        'title': _(u'Partner Management'), # optional
        'name': _(u'Partner Management'),
        'apps': ['gateway'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-open'], # optional
        'show_apps': False, # optional
    },
    2: {
        'title': _(u'Dial PLan Management'), # optional
        'name': _(u'Dial PLan Management'),
        'apps': ['dialplan'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-closed'], # optional
        'show_apps': False, # optional
    },
    3: {
        'title': _(u'FreeSWITCH Servers'), # optional
        'name': _(u'FreeSWITCH Servers'),
        'apps': ['server','acl','sites'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-closed'], # optional
        'show_apps': False, # optional
    },
    4: {
        'title': _(u'Configuration'), # optional
        'name': _(u'Configuration'),
        'apps': ['grappelli','app_plugins'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-closed'], # optional
        'show_apps': True, # optional
    }
}

user_site.groups = {
    0: {
        'title': _(u'User Management Administration'), # optional
        'name': 'User Management',
        'apps': ['auth'],
        #'template': 'custom/index_group_usermanagement.html', # optional
        'classes': ['collapse-open'], # optional
        'show_apps': True, # optional
    },
    1: {
        'name': _(u'Configuration'),
        'apps': ['site', 'l10n']
    }
}

user_site.collections = {
    0: {
        'title': 'User Admin',
        'groups': [0,1]
    },
}