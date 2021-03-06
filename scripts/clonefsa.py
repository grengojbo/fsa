#!/usr/bin/env python
# encoding: utf-8
"""
clonefsa.py

Created by jbo on 2009-12-12.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.

Then run:
    python clonefsa.py

"""

import os
from os.path import join, dirname
import shutil
from random import choice
import re
from optparse import OptionParser
import string
import settings

__VERSION__ = "0.1"

def parse_command_line():
    usage = 'usage: %prog [options]'
    version = 'Version: %prog ' + '%s' % __VERSION__
    parser = OptionParser(usage=usage, version=version)

    parser.add_option('-s', '--site', action='store',type='string', default='store',
                      dest='site_name', help="Top level directory name for the site. [default: %default]")

    parser.add_option('-l', '--localsite', action='store',type='string', default='localsite',
                      dest='local_site_name', help="Name for the local application stub. [default: %default]")


    opts, args = parser.parse_args()

    return opts, args

def install_pil():
    os.system('pip install %s' % pil_requirements)
s
def media_copy():
    """docstring for media_copy"""
    import grappelli
    from django.contrib import admin
    src_g = join(dirname(grappelli.__path__[0]), 'grappelli/media')
    src_admin = join(dirname(admin.__file__), 'media')
    dest_media = join(settings.PROJECT_ROOT, 'media')
    #os.path.isdir()
    #os.mkdir()
    # /home/www/u00014/test.linktel.com.ua/www
    #crypt.crypt('freeswitch','freeswitch') 
    # frpOsE5ExXNZw
    #/ cp -f -R /home/www/u00014/.virtualenvs/test.linktel.com.ua/lib/python2.5/site-packages/django/contrib/admin/media/*  /home/www/u00014/test.linktel.com.ua/www/media/admin
    # cp -f -R /home/www/u00014/.virtualenvs/test.linktel.com.ua/src/django-grappelli/grappelli/media/* /home/www/u00014/test.linktel.com.ua/www/media/admin
    #'cp -R /Users/jbo/.virtualenvs/fs_test/src/django-grappelli/grappelli/templates ./'


def setup_fsa(site_name, local_site_name):
    """
    Do the final configs for FreeSWITCH Admin
    """
    #os.system('cd %s && python manage.py satchmo_copy_static' % site_name)
    os.system('cd %s && python manage.py syncdb' % site_name) 
    os.system('cd %s && python manage.py loaddata l10n_data testsite server server_conf gateway sipprofile' % site_name)
    os.system('cd %s && python manage.py loaddata currency_data fsa_grappelli.json --settings=settings' % site_name)
    os.system('cd %s && python manage.py loaddata  currency_default tariffplan --settings=settings' % site_name)
    os.system('cd %s && python manage.py migrate dialplan' % site_name)
    os.system('cd %s && python manage.py migrate cdr' % site_name)
    os.system('cd %s && python manage.py migrate prepaid' % site_name)
    os.system('cd %s && python manage.py migrate directory' % site_name)
    #os.system('cd %s && python manage.py migrate ' % site_name)
    #os.system('cd %s && python manage.py loaddata fsa_grappelli.json --settings=settings' % site_name)
    #os.system('cd %s && python manage.py loaddata grappelli_help.json --settings=settings' % site_name)
    # acl extension context alias
    #os.system('cd %s && python manage.py loaddata tariffplan --settings=settings' % site_name)
    #os.system('cd %s && ' % site_name)
    #os.system('cd %s && python manage.py loaddata test_prepaid' % site_name)
    #os.system('cd %s && python manage.py loaddata acl ' % site_name)
    #os.system('cd %s && python manage.py satchmo_rebuild_pricing' % site_name)

if __name__ == '__main__':
    opts, args = parse_command_line()

    errors = []
    dest_dir = os.path.join('./',opts.site_name)
    setup_fsa(opts.site_name, opts.local_site_name)
    print "Store installation complete."
    print "You may run the server by typying: \n cd %s \n python manage.py runserver" % opts.site_name