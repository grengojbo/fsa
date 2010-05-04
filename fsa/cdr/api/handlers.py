# -*- mode: python; coding: utf-8; -*- 
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
#from fsa.directory.models import Endpoint
#from fsa.numberplan.models import NumberPlan
from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.db import transaction
from fsa.cdr.models import Cdr
from xmlrpclib import ServerProxy
from livesettings import ConfigurationSettings, config_value
from BeautifulSoup import BeautifulStoneSoup as Soup
from fsa.server.models import Server
from decimal import Decimal
from bursar.numbers import trunc_decimal
import time, datetime
import urllib

log = logging.getLogger('fsa.cdr.api.handlers')

class CdrHandler(BaseHandler):

    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST')
    model = Cdr
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('accountcode', 'caller_id_number', 'destination_number', 'billsec', 'cash', 'start_timestamp', 'hangup_cause', 'direction', 'lcr_rate', 'nibble_rate',)

    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, start=0, limit=50, phone=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        #log.debug("read endpoint % s" % account)
        base = Cdr.objects
        if request.GET.get("start"):
            start = request.GET.get("start")
        if request.GET.get("limit"):
            limit = int(request.GET.get("limit"))
            limit += int(start)
        try:
            if phone is not None:
                server = ServerProxy("http://%s:%s@%s:%s" % (config_value('SERVER', 'rcpuser'), config_value('SERVER', 'rcppasswd'), config_value('SERVER', 'rcphost'), config_value('SERVER', 'rcpport')))
                log.debug('connect to server: %s' % config_value('SERVER', 'rcpuser'))
                qphone = "%s default as xml" % phone
                resp = server.freeswitch.api("lcr", qphone)
                xml_resp = Soup(resp)
                return {"count": 1, "rate": xml_resp.row.rate.string}
            else:
                resp = base.filter(site__name__iexact=request.user)[start:limit]
                count = base.filter(site__name__iexact=request.user).count()
                return {"count": count, "lcr": resp}
        except:
            return rc.NOT_HERE

    #transaction.commit_on_success
    def create(self, request):
        time_format = "%Y-%m-%d %H:%M:%S"
        attrs = self.flatten_dict(request.POST)
        log.debug(attrs.get('cdr'))
        #xml_cdr = Soup(request.raw_post_data)
        xml_cdr = Soup(attrs.get('cdr'))
        #l.debug("billsec: %i %i" % xml_cdr.cdr.variables.billsec, xml_cdr.cdr.variables.billmsec)
        
        new_cdr = Cdr(caller_id_name = xml_cdr.cdr.callflow.caller_profile.caller_id_name.string, caller_id_number = xml_cdr.cdr.callflow.caller_profile.caller_id_number.string)
        if xml_cdr.cdr.variables.accountcode is not None:
            log.debug("accountcode %s" % xml_cdr.cdr.variables.accountcode)
            new_cdr.accountcode = xml_cdr.cdr.variables.accountcode.string
        if xml_cdr.cdr.variables.sip_received_ip is not None:
            log.debug("sip_received_ip %s" % xml_cdr.cdr.variables.sip_received_ip.string)
            new_cdr.sip_received_ip = xml_cdr.cdr.variables.sip_received_ip.string
        if xml_cdr.cdr.variables.number_alias is not None:
            log.debug("number_alias %s" % xml_cdr.cdr.variables.number_alias.string)
            new_cdr.number_alias = xml_cdr.cdr.variables.number_alias.string
        if xml_cdr.cdr.variables.lcr_rate is not None:
            log.debug("lcr_rate %s" % xml_cdr.cdr.variables.lcr_rate.string)
            new_cdr.lcr_rate = trunc_decimal(xml_cdr.cdr.variables.lcr_rate.string, 2)
        if xml_cdr.cdr.variables.nibble_rate is not None:
            log.debug("nibble_rate %s" % xml_cdr.cdr.variables.nibble_rate.string)
            new_cdr.nibble_rate = trunc_decimal(xml_cdr.cdr.variables.nibble_rate.string, 2)
        if xml_cdr.cdr.variables.lcr_carrier is not None:
            log.debug("lcr_carrier %s" % xml_cdr.cdr.variables.lcr_carrier.string)
            new_cdr.lcr_carrier = xml_cdr.cdr.variables.lcr_carrier.string
        if xml_cdr.cdr.channel_data.direction is not None:
            log.debug("direction %s" % xml_cdr.cdr.channel_data.direction.string)
            if xml_cdr.cdr.channel_data.direction.string == 'inbound':
                new_cdr.direction = 1
            elif xml_cdr.cdr.channel_data.direction.string == 'outbound':
                new_cdr.direction = 2
        new_cdr.destination_number = xml_cdr.cdr.callflow.caller_profile.destination_number.string
        log.debug("destination_number %s" % xml_cdr.cdr.callflow.caller_profile.destination_number.string)
        new_cdr.context = xml_cdr.cdr.callflow.caller_profile.context.string
        log.debug("context %s" % xml_cdr.cdr.callflow.caller_profile.context.string)
        new_cdr.start_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.start_stamp.string), time_format)))
        log.debug("start_stamp: %s" % new_cdr.start_timestamp)
        
        new_cdr.answer_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.answer_stamp.string), time_format)))
        #log.debug("answer_stamp: %s" % xml_cdr.cdr.variables.answer_stamp.string)
        new_cdr.end_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.end_stamp.string), time_format)))
        #log.debug("end_stamp: %s" % xml_cdr.cdr.variables.end_stamp.string)
        new_cdr.duration = xml_cdr.cdr.variables.duration.string
        log.debug("duration: %s" % xml_cdr.cdr.variables.duration.string)
        new_cdr.billsec = int(xml_cdr.cdr.variables.billsec.string)
        log.debug("billsec %s" % xml_cdr.cdr.variables.billsec.string)
        new_cdr.hangup_cause = xml_cdr.cdr.variables.hangup_cause.string
        log.debug("hangup_cause %s" % xml_cdr.cdr.variables.hangup_cause.string)
        new_cdr.uuid = xml_cdr.cdr.callflow.caller_profile.uuid.string
        log.debug("uuid %s" % xml_cdr.cdr.callflow.caller_profile.uuid.string)
        new_cdr.read_codec = xml_cdr.cdr.variables.read_codec.string
        log.debug("read_codec %s" % new_cdr.read_codec)
        new_cdr.write_codec = xml_cdr.cdr.variables.write_codec.string
        log.debug("write_codec %s" % new_cdr.write_codec)
        #sip_user_agent
        if new_cdr.lcr_rate > Decimal("0") and new_cdr.nibble_rate > Decimal("0") and new_cdr.billsec > 0:
            new_cdr.cash = new_cdr.nibble_rate/60*new_cdr.billsec
            new_cdr.marja = new_cdr.cash-(new_cdr.lcr_rate/60*new_cdr.billsec)
            try:
                from fsb.billing.models import Balance
                bal = Balance.objects.get(accountcode__username__exact=new_cdr.accountcode)
                bal.cash -= new_cdr.cash
                bal.save()
            except:
                pass
        #<endpoint_disposition>ANSWER</endpoint_disposition>
        #<proto_specific_hangup_cause>sip%3A200</proto_specific_hangup_cause>
        #<sip_hangup_phrase>OK</sip_hangup_phrase>
##        <sip_use_codec_name>GSM</sip_use_codec_name>
##        <sip_use_codec_rate>8000</sip_use_codec_rate>
##        <sip_use_codec_ptime>20</sip_use_codec_ptime>
##        <read_codec>GSM</read_codec>
##        <read_rate>8000</read_rate>
##        <write_codec>GSM</write_codec>
##        <write_rate>8000</write_rate>
        new_cdr.save()
        
        log.debug("caller_id_name %s" % new_cdr.caller_id_name)
        log.debug("caller_id_number %s" % new_cdr.caller_id_number)
        #log.debug("bridge_channel %s" % new_cdr.bridge_channel)
        #resp = rc.CREATED
        resp = rc.ALL_OK
        #resp.write(endpoint)
        return resp
