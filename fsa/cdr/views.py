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
from currency.fields import *
from currency.money import Money
from currency.models import Currency
from bursar.numbers import trunc_decimal
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

#render_to('server/fs.xml')
def set_cdr(request):
    """
    load XML CDR
    http://wiki.freeswitch.org/wiki/Mod_xml_cdr
    """
    time_format = "%Y-%m-%d %H:%M:%S"
    #l.debug("xml_cdr %s" % request.POST)
    
    xml_cdr = Soup(request.raw_post_data)
    #l.debug("billsec: %i %i" % xml_cdr.cdr.variables.billsec, xml_cdr.cdr.variables.billmsec)
    new_cdr = Cdr(caller_id_name = xml_cdr.cdr.callflow.caller_profile.caller_id_name.string, caller_id_number = xml_cdr.cdr.callflow.caller_profile.caller_id_number.string)
    if xml_cdr.cdr.variables.accountcode.string is not None:
        l.debug("accountcode %s" % xml_cdr.cdr.variables.accountcode.string)
        new_cdr.accountcode = xml_cdr.cdr.variables.accountcode.string
    if xml_cdr.cdr.variables.nibble_account.string is not None:
        l.debug("nibble_account %s" % xml_cdr.cdr.variables.nibble_account.string)
        new_cdr.nibble_account = xml_cdr.cdr.variables.nibble_account.string
        
    if xml_cdr.cdr.variables.sip_received_ip.string is not None:
        l.debug("sip_received_ip %s" % xml_cdr.cdr.variables.sip_received_ip.string)
        new_cdr.sip_received_ip = xml_cdr.cdr.variables.sip_received_ip.string
    if xml_cdr.cdr.variables.number_alias.string is not None:
        l.debug("number_alias %s" % xml_cdr.cdr.variables.number_alias.string)
        new_cdr.number_alias = xml_cdr.cdr.variables.number_alias.string
    if xml_cdr.cdr.variables.lcr_rate.string is not None:
        l.debug("lcr_rate %s" % xml_cdr.cdr.variables.lcr_rate.string)
        new_cdr.lcr_rate = trunc_decimal(xml_cdr.cdr.variables.lcr_rate.string, 2)
    if xml_cdr.cdr.variables.lcr_carrier.string is not None:
        l.debug("lcr_carrier %s" % xml_cdr.cdr.variables.lcr_carrier.string)
        new_cdr.lcr_carrier = xml_cdr.cdr.variables.lcr_carrier.string
    if xml_cdr.cdr.channel_data.direction.string is not None:
        l.debug("direction %s" % xml_cdr.cdr.variables.direction.string)
        if xml_cdr.cdr.channel_data.direction.string == 'inbound':
            new_cdr.direction = 1
        elif xml_cdr.cdr.channel_data.direction.string == 'outbound':
            new_cdr.direction = 2
    new_cdr.destination_number = xml_cdr.cdr.callflow.caller_profile.destination_number.string
    new_cdr.context = xml_cdr.cdr.callflow.caller_profile.context.string
    new_cdr.start_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.start_stamp.string), time_format)))
    #new_cdr.start_timestamp = '2009-02-24 16:47:54.099098'
    new_cdr.answer_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.answer_stamp.string), time_format)))
    new_cdr.end_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.end_stamp.string), time_format)))
    new_cdr.duration = xml_cdr.cdr.variables.duration.string
    new_cdr.billsec = int(xml_cdr.cdr.variables.billsec.string)
    new_cdr.hangup_cause = xml_cdr.cdr.variables.hangup_cause.string
    new_cdr.uuid = xml_cdr.cdr.callflow.caller_profile.uuid.string
    new_cdr.read_codec = xml_cdr.cdr.variables.read_codec.string
    new_cdr.write_codec = xml_cdr.cdr.variables.write_codec.string
    new_cdr.save()

    
    #l.debug("caller_id_name %s" % new_cdr.caller_id_name)
    #l.debug("caller_id_number %s" % new_cdr.caller_id_number)
    #l.debug("destination_number %s" % xml_cdr.cdr.callflow.caller_profile.destination_number.string)
    #l.debug("context %s" % xml_cdr.cdr.callflow.caller_profile.context.string)
    l.debug("start_stamp: %s" % new_cdr.start_timestamp)
    #l.debug("answer_stamp: %s" % xml_cdr.cdr.variables.answer_stamp.string)
    #l.debug("end_stamp: %s" % xml_cdr.cdr.variables.end_stamp.string)
    #l.debug("duration: %s" % xml_cdr.cdr.variables.duration.string)
    #l.debug("billsec %s" % xml_cdr.cdr.variables.billsec.string)
    #l.debug("hangup_cause %s" % xml_cdr.cdr.variables.hangup_cause.string)
    #l.debug("uuid %s" % xml_cdr.cdr.callflow.caller_profile.uuid.string)
    ##l.debug("bridge_channel %s" % new_cdr.bridge_channel)
    #l.debug("read_codec %s" % new_cdr.read_codec)
    #l.debug("write_codec %s" % new_cdr.write_codec)

    key_value = name = 'result'
    xml_context = '<result status="not found" />'
    return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')

#render_to('cdr/xml_cdr.conf.xml')
def get_xml_conf(request):
    """ 
    reguest -- 
    """
    es = Server.objects.get(name=request.POST.get('hostname'), enabled=True)
    return request.Context({'hostname':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn, 'xc': es.options['xml_cdr']}).render_response('cdr/xml_cdr.conf.xml')

