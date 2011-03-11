# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#from fsa.server.models import Server
from bursar.fields import CurrencyField
import datetime
from decimal import Decimal
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
#from currency.fields import *
#from currency.money import Money
#from currency.models import Currency
from decimal import Decimal

__author__ = '$Author:$'
__revision__ = '$Revision:$'

D_STATUS = ((0, _(u'bouth')),
           (1,_(u'inbound')),
           (2,_(u'outbound')),
        )
P_STATUS = ((0, _(u'необработан')),
           (1,_(u'обработан')),
           (2,_(u'обрабатывается')),
        )
# Create your models here.
class Cdr(models.Model):
    # TODO: добавилось новое поле  UPDATE billusec=billsec*1000000 where billusec=0 and billsec>0;
    # если direction = 0 то неопределено откуда звонок
    accountcode = models.CharField(_(u'Accaunt'), max_length=60)
    caller_id_name = models.CharField(_(u'Caller Name'), max_length=240)
    caller_id_number = models.CharField(_(u'Caller Number'), max_length=240)
    destination_number = models.CharField(_(u'Destinatio'), max_length=240)
    context = models.CharField(_(u'Context'), max_length=240)
    start_timestamp = models.DateTimeField(_(u'Start call'), help_text=_(u'Date/time that the call was initiated.'))
    answer_timestamp = models.DateTimeField(_(u'Answered'), help_text=_(u'Date/time that the far end of the call was actually answered.'))
    end_timestamp = models.DateTimeField(_(u'End call'), help_text=_(u'Date/time that the call was terminated.'))
    duration = models.IntegerField(_(u'Total duration'), help_text=_(u'Total call duration in seconds.'))
    billsec = models.PositiveIntegerField(_(u'Duration'), help_text=_(u'Billable call duration in seconds. Billable time does not include call time spent in "early media" prior to the far end answering the call.'))
    hangup_cause = models.CharField(_(u'Hangup'), max_length=135)
    # TODO: добавить уникальность поля
    uuid = models.CharField(_(u'UUID'), max_length=108)
    #uuid = models.CharField(_(u'UUID'), max_length=108, unique=True)
    nibble_account = models.PositiveIntegerField(_(u'Billing ID account'), default=0)
    sip_received_ip = models.IPAddressField(_(u'Received IP'), default='127.0.0.1')
    number_alias = models.CharField(_(u'Phone alias'), max_length=12, blank=True, null=True)
    #lcr_rate = CurrencyField(_("Lcr Rate"), max_digits=18, decimal_places=2, default=Decimal("0.0"), display_decimal=4)
    lcr_rate = models.DecimalField(_("Lcr Rate"), max_digits=18, decimal_places=4, default=Decimal("0.0"))
    nibble_rate = models.DecimalField(_("Rate"), max_digits=18, decimal_places=4, default=Decimal("0.0"))
    cash = models.DecimalField(_("Cash"), max_digits=18, decimal_places=6, default=Decimal("0.0"))
    nibble_current_balance = models.DecimalField(_("Current Balance"), max_digits=18, decimal_places=6, default=Decimal("0.0"))
    nibble_total_billed =  models.DecimalField(_("Money Billed"), max_digits=18, decimal_places=6, default=Decimal("0.0"))
    nibble_tariff = models.PositiveSmallIntegerField(_('Tariff'), default=0)
    billusec = models.PositiveIntegerField(_('Billing Microsec'), default=0)
    marja = models.DecimalField(_("Marja"), max_digits=18, decimal_places=6, default=Decimal("0.0"))
    lcr_carrier = models.CharField(_(u'Gateway'), max_length=50, default='local')
    direction = models.PositiveSmallIntegerField(_(u'Direction'), max_length=1, choices=D_STATUS, default=0, blank=False)
    #bleg_uuid = models.CharField(max_length=108)
    #bridge_channel = models.CharField(max_length=108, blank=True)
    # TODO: add default value
    read_codec =  models.CharField(_(u'Read codec'), max_length=10)
    # TODO: add default value
    write_codec = models.CharField(_(u'Write codec'), max_length=10)

    lprice =  models.DecimalField('LCR Price', default=Decimal("0"), max_digits=18, decimal_places=4)
    lprice_currency = models.CharField(_(u'LCR Currency name'), max_length=3, default="USD")
    lcr_name = models.CharField(_(u'Country'), max_length=200, default="local")
    lcr_digits = models.PositiveIntegerField(_(u'Digits'), default=0)
    procesed = models.PositiveSmallIntegerField(_(u'Procesed'), max_length=1, choices=P_STATUS, default=0, blank=False)
    site_id = models.PositiveIntegerField(_(u'Site'), default=1)
    gw_id = models.PositiveIntegerField(_(u'Gateway ID'), default=0)
    gw = models.CharField(_(u'Gateway'), max_length=50, default="local")
    rtp_audio_in_raw_bytes = models.PositiveIntegerField(verbose_name='rtp_audio_in_raw_bytes', default=0)
    rtp_audio_in_media_bytes = models.PositiveIntegerField(verbose_name='rtp_audio_in_media_bytes', default=0)
    rtp_audio_in_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_packet_count', default=0)
    rtp_audio_in_media_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_media_packet_count', default=0)
    rtp_audio_in_skip_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_skip_packet_count', default=0)
    rtp_audio_in_jb_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_jb_packet_count', default=0)
    rtp_audio_in_dtmf_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_dtmf_packet_count', default=0)
    rtp_audio_in_cng_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_cng_packet_count', default=0)
    rtp_audio_in_flush_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_in_flush_packet_count', default=0)
    rtp_audio_out_raw_bytes = models.PositiveIntegerField(verbose_name='rtp_audio_out_raw_bytes', default=0)
    rtp_audio_out_media_bytes = models.PositiveIntegerField(verbose_name='rtp_audio_out_media_bytes', default=0)
    rtp_audio_out_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_out_packet_count', default=0)
    rtp_audio_out_media_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_out_media_packet_count', default=0)
    rtp_audio_out_skip_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_out_skip_packet_count', default=0)
    rtp_audio_out_dtmf_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_out_dtmf_packet_count', default=0)
    rtp_audio_out_cng_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_out_cng_packet_count', default=0)
    rtp_audio_rtcp_packet_count = models.PositiveIntegerField(verbose_name='rtp_audio_rtcp_packet_count', default=0)
    rtp_audio_rtcp_octet_count = models.PositiveIntegerField(verbose_name='rtp_audio_rtcp_octet_count', default=0)


    #sip_user_agent call_clientcode
    #sip_rtp_rxstat sip_rtp_txstat sofia_record_file
    class Meta:
        db_table = u'cdr'
        verbose_name = _(u'CDR')
        verbose_name_plural = _(u'CDRs')

    def __unicode__(self):
        return "{0} - {1}".format(self.caller_id_number, self.destination_number)

    @property
    def username(self):
        return self.accountcode

    @property
    def phone(self):
        return self.caller_id_number

    @property
    def ipaddr(self):
        return self.sip_received_ip

# class Conf(models.Model):
#     name = models.CharField(_(u'Name'), max_length=25)
#     server = models.ForeignKey(Server)
#     url = models.CharField(_(u'URL'), max_length=50, default="http://localhost/cdr/set/", help_text=_(u"the url to post to if blank web posting is disabled"))
#     user =  models.CharField(_(u'User'), max_length=25, blank=True, help_text=_(u'optional: credentials to send to web server'))
#     passwd =  models.CharField(_(u'Password'), max_length=25, blank=True, help_text=_(u'optional: credentials to send to web server'))
#     retries =  models.PositiveIntegerField(_(u'Retries'), default=2, help_text=_(u'the total number of retries (not counting the first try) to post to webserver incase of failure'))
#     delay =  models.PositiveIntegerField(_(u'Delay'), blank=True, default=1, help_text=_(u'delay between retries in seconds, default is 5 seconds'))
#     log_dir =  models.CharField(_(u'Log DIR'), max_length=240, blank=True, help_text=_(u'optional: if not present we do not log every record to disk either an absolute path, a relative path assuming ${prefix}/logs or a blank value will default to ${prefix}/logs/xml_cdr '))
#     log_b_leg =  models.BooleanField(_(u'Log b leg'), default=False, help_text=_(u'optional: if not present we do log the b leg true or false if we should create a cdr for the b leg of a call'))
#     prefix_a_leg =  models.BooleanField(_(u'Prefix a leg'), default=True, help_text=_(u'optional: if not present, all filenames are the uuid of the call true or false if a leg files are prefixed "a_"'))
#     #encode = models.BooleanField(_(u'Encode'), default=True, help_text=_(u'encode the post data may be true for url encoding, false for no encoding or base64 for base64 encoding'))
#     lighttpd =  models.BooleanField(_(u'Lighttpd'),default=True, help_text=_(u'optional: set to true to disable Expect: 100-continue lighttpd requires this setting'))
#     err_log =  models.CharField(_(u'Error Log DIR'), max_length=240, blank=True, default="log/xml_cdr", help_text=_(u'optional: full path to the error log dir for failed web posts if not specified its the same as log-dir, either an absolute path, a relative path assuming ${prefix}/logs or a blank or omitted value will default to ${prefix}/logs/xml_cdr'))
#     cdr_ca =  models.BooleanField(_(u'Disable CA'), default=True, help_text=_(u'optional: if enabled this will disable CA root certificate checks by libcurl note: default value is disabled. only enable if you want this!'))
#     enabled = models.BooleanField(_(u'Enable'), default=False)
#
#     def __unicode__(self):
#         return self.name
#
#     class Meta:
#         db_table = u'cdr_conf'
