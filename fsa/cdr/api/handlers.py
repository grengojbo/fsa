# -*- mode: python; coding: utf-8; -*-
from piston.handler import PaginatedCollectionBaseHandler
from piston.utils import rc
#from piston.doc import generate_doc
import logging
#from fsa.directory.models import Endpoint
#from fsa.numberplan.models import NumberPlan
from django.db import transaction
from fsa.cdr.models import Cdr
from BeautifulSoup import BeautifulStoneSoup as Soup
from fsa.directory.models import Endpoint
from fsb.billing.models import Balance
from decimal import Decimal
from bursar.numbers import trunc_decimal
import time, datetime
import urllib

log = logging.getLogger('fsa.cdr.api.handlers')

class CdrHandler(PaginatedCollectionBaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST')
    model = Cdr
    #anonymous = 'AnonymousBlogpostHandler'
    fields = (
    'username', 'phone', 'destination_number', 'billsec', 'cash', 'start_timestamp', 'hangup_cause', 'direction',
    'lcr_rate', 'nibble_rate', 'answer_timestamp', 'end_timestamp', 'ipaddr',)

    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, phone=None, account=None, start_date=None, end_date=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        self.resource_name = 'cdr'
        try:
            if phone is not None and start_date is not None and end_date is not None:
                fend_date = "{0} 23:59:59".format(end_date)
                fstart_date = "{0} 00:00:00".format(start_date)
                endpoint = Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)
                self.resources = Cdr.objects.filter(caller_id_number__exact=endpoint.uid,
                                                    time_stamp__range=(fstart_date, fend_date))
                return super(CdrHandler, self).read(request)
            elif account is not None and start_date is not None and end_date is not None:
                fend_date = "{0} 23:59:59".format(end_date)
                fstart_date = "{0} 00:00:00".format(start_date)
                accountcode = Balance.objects.get(accountcode__username__exact=account, site__name__exact=request.user)
                self.resources = Cdr.objects.filter(accountcode__exact=accountcode.accountcode.username,
                                                    time_stamp__range=(fstart_date, fend_date))
                return super(CdrHandler, self).read(request)
            elif phone is not None:
                endpoint = Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)
                self.resources = Cdr.objects.filter(caller_id_number__exact=endpoint.uid)
                return super(CdrHandler, self).read(request)
            elif account is not None:
                accountcode = Balance.objects.get(accountcode__username__exact=account, site__name__exact=request.user)
                self.resources = Cdr.objects.filter(accountcode__exact=accountcode.accountcode.username)
                return super(CdrHandler, self).read(request)
            else:
                return rc.NOT_HERE
        except:
            return rc.NOT_HERE

    @transaction.commit_on_success
    def create(self, request):
        time_format = "%Y-%m-%d %H:%M:%S"
        attrs = self.flatten_dict(request.POST)
        user = request.user

        #log.debug(attrs.get('cdr'))

        #xml_cdr = Soup(request.raw_post_data)
        #parser = etree.XMLParser(remove_blank_text=True)
        #root = "<root><tag>text</tag><aa><bb>bbb</bb><cc>ccc</cc></aa></root>"
        #tree = etree.fromstring(root, parser)
        #return rc.NOT_HERE
        if user.has_perm("cdr.add_cdr"):
            try:
                xml_cdr = Soup(attrs.get('cdr'))

                new_cdr = Cdr(caller_id_name=xml_cdr.cdr.callflow.caller_profile.caller_id_name.string,
                              caller_id_number=xml_cdr.cdr.callflow.caller_profile.caller_id_number.string)
                #new_cdr.procesed = 1
                # TODO: New stats (n CDRs) rtcp_packet_count and rtcp_octet_count
                if xml_cdr.cdr.variables.lcr_rate is not None:
                    log.debug("lcr_rate %s" % xml_cdr.cdr.variables.lcr_rate.string)
                    new_cdr.lcr_rate = trunc_decimal(xml_cdr.cdr.variables.lcr_rate.string, 4)
                if xml_cdr.cdr.variables.lcr_currency is not None:
                    new_cdr.lprice_currency = xml_cdr.cdr.variables.lcr_currency.string
                else:
                    new_cdr.lprice_currency = "UAH"
                if xml_cdr.cdr.variables.lcr_price is not None:
                    new_cdr.lprice = trunc_decimal(xml_cdr.cdr.variables.lcr_price.string, 4)
                else:
                    new_cdr.lprice = trunc_decimal("0.18", 4)

                if xml_cdr.cdr.variables.lcr_name is not None:
                    new_cdr.lcr_name = xml_cdr.cdr.variables.lcr_name.string
                if xml_cdr.cdr.variables.lcr_digits is not None:
                    new_cdr.lcr_digits = int(xml_cdr.cdr.variables.lcr_digits.string)
                if xml_cdr.cdr.variables.lcr_carrier is not None:
                    log.debug("lcr_carrier %s" % xml_cdr.cdr.variables.lcr_carrier.string)
                    new_cdr.lcr_carrier = xml_cdr.cdr.variables.lcr_carrier.string

                if xml_cdr.cdr.variables.lcr_direction is not None and xml_cdr.cdr.variables.lcr_direction.string == 'in':
                    # входящий звонок
                    new_cdr.direction = 1
                    new_cdr.nibble_rate = trunc_decimal("0.0", 4)
                elif xml_cdr.cdr.variables.lcr_direction is not None and xml_cdr.cdr.variables.lcr_direction.string == 'out':
                    # исходящий звонок
                    new_cdr.direction = 2
                    if xml_cdr.cdr.variables.nibble_rate is not None:
                        log.debug("nibble_rate %s" % xml_cdr.cdr.variables.nibble_rate.string)
                        new_cdr.nibble_rate = trunc_decimal(xml_cdr.cdr.variables.nibble_rate.string, 4)
                    else:
                        new_cdr.nibble_rate = trunc_decimal("0.0", 4)
                else:
                    new_cdr.direction = 0
                    new_cdr.nibble_rate = trunc_decimal("0.0", 4)
                if xml_cdr.cdr.variables.nibble_current_balance is not None:
                    #<nibble_total_billed>0.087786</nibble_total_billed>
                    log.debug("nibble_current_balance %s" % xml_cdr.cdr.variables.nibble_current_balance.string)
                    new_cdr.nibble_current_balance = trunc_decimal(xml_cdr.cdr.variables.nibble_current_balance.string, 6)
                if xml_cdr.cdr.variables.nibble_tariff is not None:
                    new_cdr.nibble_tariff = int(xml_cdr.cdr.variables.nibble_tariff.string)
                if xml_cdr.cdr.variables.nibble_account is not None:
                    new_cdr.nibble_account = int(xml_cdr.cdr.variables.nibble_account.string)
                if xml_cdr.cdr.variables.site_id is not None:
                    new_cdr.site_id = int(xml_cdr.cdr.variables.site_id.string)
                if xml_cdr.cdr.variables.billusec is not None:
                    new_cdr.billusec = int(xml_cdr.cdr.variables.billusec.string)
                    log.debug("billusec: %i" % int(xml_cdr.cdr.variables.billusec.string))

                #elif xml_cdr.cdr.channel_data.direction is not None:
                    #log.debug("direction %s" % xml_cdr.cdr.channel_data.direction.string)
                    #if xml_cdr.cdr.channel_data.direction.string == 'inbound':
                #new_cdr.direction = 1
                    #elif xml_cdr.cdr.channel_data.direction.string == 'outbound':
                #new_cdr.direction = 2
                #l.debug("billsec: %i %i" % xml_cdr.cdr.variables.billsec, xml_cdr.cdr.variables.billmsec)

                if xml_cdr.cdr.variables.accountcode is not None:
                    log.debug("accountcode %s" % xml_cdr.cdr.variables.accountcode.string)
                    new_cdr.accountcode = xml_cdr.cdr.variables.accountcode.string
                else:
                    new_cdr.accountcode = "none"
                if xml_cdr.cdr.variables.sip_received_ip is not None:
                    log.debug("sip_received_ip %s" % xml_cdr.cdr.variables.sip_received_ip.string)
                    new_cdr.sip_received_ip = xml_cdr.cdr.variables.sip_received_ip.string
                if xml_cdr.cdr.variables.number_alias is not None:
                    log.debug("number_alias %s" % xml_cdr.cdr.variables.number_alias.string)
                    new_cdr.number_alias = xml_cdr.cdr.variables.number_alias.string

                new_cdr.destination_number = xml_cdr.cdr.callflow.caller_profile.destination_number.string
                log.debug("destination_number %s" % xml_cdr.cdr.callflow.caller_profile.destination_number.string)
                new_cdr.context = xml_cdr.cdr.callflow.caller_profile.context.string
                log.debug("context %s" % xml_cdr.cdr.callflow.caller_profile.context.string)
                new_cdr.start_timestamp = datetime.datetime.utcfromtimestamp(
                        time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.start_stamp.string), time_format)))
                log.debug("start_stamp: %s" % new_cdr.start_timestamp)

                if xml_cdr.cdr.variables.answer_stamp is not None:
                    new_cdr.answer_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.answer_stamp.string), time_format)))
                else:
                    new_cdr.answer_timestamp = new_cdr.start_timestamp
                log.debug("answer_stamp:{0}".format(new_cdr.answer_timestamp))
                #new_cdr.end_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.end_stamp.string), time_format)))
                #log.debug("end_stamp: %s" % xml_cdr.cdr.variables.end_stamp.string)

                try:
                    new_cdr.duration = xml_cdr.cdr.variables.duration.string
                except Exception as e:
                    log.error(e)
                    new_cdr.duration = '0'
                log.debug("duration: {0}".format(new_cdr.duration))
                new_cdr.billsec = int(xml_cdr.cdr.variables.billsec.string)
                log.debug("billsec {0}".format(xml_cdr.cdr.variables.billsec.string))
                new_cdr.hangup_cause = xml_cdr.cdr.variables.hangup_cause.string
                log.debug("hangup_cause {0}".format(xml_cdr.cdr.variables.hangup_cause.string))
                new_cdr.uuid = xml_cdr.cdr.callflow.caller_profile.uuid.string
                log.debug("uuid {0}".format(xml_cdr.cdr.callflow.caller_profile.uuid.string))
                try:
                    new_cdr.read_codec = xml_cdr.cdr.variables.read_codec.string
                except Exception as e:
                    #log.error(e)
                    # TODO: add to None
                    new_cdr.read_codec = 'PCMA'
                log.debug("read_codec{0}".format(new_cdr.read_codec))
                try:
                    new_cdr.write_codec = xml_cdr.cdr.variables.write_codec.string
                except Exception as e:
                    #log.error(e)
                    new_cdr.write_codec = new_cdr.read_codec
                log.debug("write_codec {0}".format(new_cdr.write_codec))

                if xml_cdr.cdr.variables.rtp_audio_in_raw_bytes is not None:
                    new_cdr.rtp_audio_in_raw_bytes = int(xml_cdr.cdr.variables.rtp_audio_in_raw_bytes.string)
                if xml_cdr.cdr.variables.rtp_audio_in_media_bytes is not None:
                    new_cdr.rtp_audio_in_media_bytes = int(xml_cdr.cdr.variables.rtp_audio_in_media_bytes.string)
                if xml_cdr.cdr.variables.rtp_audio_in_packet_count is not None:
                    new_cdr.rtp_audio_in_packet_count = int(xml_cdr.cdr.variables.rtp_audio_in_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_media_packet_count is not None:
                    new_cdr.rtp_audio_in_media_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_in_media_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_skip_packet_count is not None:
                    new_cdr.rtp_audio_in_skip_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_in_skip_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_jb_packet_count is not None:
                    new_cdr.rtp_audio_in_jb_packet_count = int(xml_cdr.cdr.variables.rtp_audio_in_jb_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_dtmf_packet_count is not None:
                    new_cdr.rtp_audio_in_dtmf_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_in_dtmf_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_cng_packet_count is not None:
                    new_cdr.rtp_audio_in_cng_packet_count = int(xml_cdr.cdr.variables.rtp_audio_in_cng_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_in_flush_packet_count is not None:
                    new_cdr.rtp_audio_in_flush_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_in_flush_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_out_raw_bytes is not None:
                    new_cdr.rtp_audio_out_raw_bytes = int(xml_cdr.cdr.variables.rtp_audio_out_raw_bytes.string)
                if xml_cdr.cdr.variables.rtp_audio_out_media_bytes is not None:
                    new_cdr.rtp_audio_out_media_bytes = int(xml_cdr.cdr.variables.rtp_audio_out_media_bytes.string)
                if xml_cdr.cdr.variables.rtp_audio_out_packet_count is not None:
                    new_cdr.rtp_audio_out_packet_count = int(xml_cdr.cdr.variables.rtp_audio_out_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_out_media_packet_count is not None:
                    new_cdr.rtp_audio_out_media_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_out_media_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_out_skip_packet_count is not None:
                    new_cdr.rtp_audio_out_skip_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_out_skip_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_out_dtmf_packet_count is not None:
                    new_cdr.rtp_audio_out_dtmf_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_out_dtmf_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_out_cng_packet_count is not None:
                    new_cdr.rtp_audio_out_cng_packet_count = int(
                            xml_cdr.cdr.variables.rtp_audio_out_cng_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_rtcp_packet_count is not None:
                    new_cdr.rtp_audio_rtcp_packet_count = int(xml_cdr.cdr.variables.rtp_audio_rtcp_packet_count.string)
                if xml_cdr.cdr.variables.rtp_audio_rtcp_octet_count is not None:
                    new_cdr.rtp_audio_rtcp_octet_count = int(xml_cdr.cdr.variables.rtp_audio_rtcp_octet_count.string)

                if xml_cdr.cdr.variables.nibble_total_billed is not None:
                    #<nibble_total_billed>0.087786</nibble_total_billed>
                    log.debug("nibble_total_billed {0}".format(xml_cdr.cdr.variables.nibble_total_billed.string))
                    new_cdr.nibble_total_billed = trunc_decimal(xml_cdr.cdr.variables.nibble_total_billed.string, 6)
                #sip_user_agent
                #if new_cdr.lcr_rate > Decimal("0") and new_cdr.nibble_rate > Decimal("0") and new_cdr.billsec > 0:
                if new_cdr.lcr_rate > Decimal("0") and new_cdr.billusec > 0:
                    #new_cdr.cash = new_cdr.nibble_rate/60*new_cdr.billsec
                    new_cdr.cash = new_cdr.lcr_rate / 1000000 / 60 * new_cdr.billusec
                if new_cdr.cash is not None and new_cdr.nibble_total_billed is not None:
                    new_cdr.marja = new_cdr.cash - new_cdr.nibble_total_billed
                    #try:
                #from fsb.billing.models import Balance
                #bal = Balance.objects.get(accountcode__username__exact=new_cdr.accountcode)
                #bal.cash -= new_cdr.cash
                #bal.save()
                    #except:
                #pass
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

                log.debug("caller_id_name {0}".format(new_cdr.caller_id_name))
                log.debug("caller_id_number {0}".format(new_cdr.caller_id_number))
                #log.debug("bridge_channel %s" % new_cdr.bridge_channel)
                #resp = rc.CREATED
                resp = rc.ALL_OK
                #resp.write(endpoint)
                return resp
            except Exception as e:
                log.error(e)
                return rc.NOT_HERE
        else:
            return rc.FORBIDDEN

