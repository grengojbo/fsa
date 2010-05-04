# -*- mode: python; coding: utf-8; -*-
#from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.cdr.models import Cdr
from fsa.server.models import Server
#from django.views.generic.list_detail import object_list
#from sugar.views.decorators import render_to
#from django.shortcuts import get_object_or_404
#from lib.helpers import reverse
from BeautifulSoup import BeautifulStoneSoup as Soup
import datetime
from decimal import Decimal
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

import time
import urllib
import logging

l = logging.getLogger('fsa.cdr.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your views here.

#render_to('cdr/cdr_csv.conf.xml')
def get_csv_conf(request):
    """ 
    reguest -- 
    """
    return {'name':'sql'}
def set_cdr(request):
    """
    load XML CDR
    http://wiki.freeswitch.org/wiki/Mod_xml_cdr
    """
    time_format = "%Y-%m-%d %H:%M:%S"
    #l.debug("xml_cdr %s" % request.POST)
    
    xml_cdr = Soup(request.raw_post_data)

#render_to('cdr/xml_cdr.conf.xml')
def get_xml_conf(request):
    """ 
    reguest -- 
    """
    es = Server.objects.get(name=request.POST.get('hostname'), enabled=True)
    return request.Context({'hostname':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn, 'xc': es.options['xml_cdr']}).render_response('cdr/xml_cdr.conf.xml')

