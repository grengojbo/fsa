# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.server.models import Server

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your models here.
class Cdr(models.Model):
    accountcode = models.CharField(_(u'Accaunt'), max_length=60)
    caller_id_name = models.CharField(_(u'Caller Name'), max_length=240)
    caller_id_number = models.CharField(_(u'Caller Number'), max_length=240)
    destination_number = models.CharField(_(u'Destinatio'), max_length=240)
    context = models.CharField(_(u'Context'), max_length=240)
    start_timestamp = models.DateTimeField(_(u'Start call'), help_text=_(u'Date/time that the call was initiated.'))
    answer_timestamp = models.DateTimeField(_(u'Answered'), help_text=_(u'Date/time that the far end of the call was actually answered.'))
    end_timestamp = models.DateTimeField(_(u'End call'), help_text=_(u'Date/time that the call was terminated.'))
    duration = models.IntegerField(_(u'Total duration'), help_text=_(u'Total call duration in seconds.'))
    billsec = models.IntegerField(_(u'Duration'), help_text=_(u'Billable call duration in seconds. Billable time does not include call time spent in "early media" prior to the far end answering the call.'))
    hangup_cause = models.CharField(_(u'Hangup'), max_length=135)
    uuid = models.CharField(_(u'UUID'), max_length=108)
    #bleg_uuid = models.CharField(max_length=108)
    #bridge_channel = models.CharField(max_length=108, blank=True)
    read_codec =  models.CharField(_(u'Read codec'), max_length=10)
    write_codec = models.CharField(_(u'Write codec'), max_length=10)
    #sip_user_agent call_clientcode
    #sip_rtp_rxstat sip_rtp_txstat sofia_record_file
    class Meta:
        db_table = u'cdr'
        verbose_name = _(u'CDR')
        verbose_name_plural = _(u'CDRs')

class Conf(models.Model):
    name = models.CharField(_(u'Name'), max_length=25)
    server = models.ForeignKey(Server)
    url = models.CharField(_(u'URL'), max_length=50, default="http://localhost/cdr/set/", help_text=_(u"the url to post to if blank web posting is disabled"))
    user =  models.CharField(_(u'User'), max_length=25, blank=True, help_text=_(u'optional: credentials to send to web server'))
    passwd =  models.CharField(_(u'Password'), max_length=25, blank=True, help_text=_(u'optional: credentials to send to web server'))
    retries =  models.PositiveIntegerField(_(u'Retries'), default=2, help_text=_(u'the total number of retries (not counting the first try) to post to webserver incase of failure'))
    delay =  models.PositiveIntegerField(_(u'Delay'), blank=True, default=1, help_text=_(u'delay between retries in seconds, default is 5 seconds'))
    log_dir =  models.CharField(_(u'Log DIR'), max_length=240, blank=True, help_text=_(u'optional: if not present we do not log every record to disk either an absolute path, a relative path assuming ${prefix}/logs or a blank value will default to ${prefix}/logs/xml_cdr '))
    log_b_leg =  models.BooleanField(_(u'Log b leg'), default=False, help_text=_(u'optional: if not present we do log the b leg true or false if we should create a cdr for the b leg of a call'))
    prefix_a_leg =  models.BooleanField(_(u'Prefix a leg'), default=True, help_text=_(u'optional: if not present, all filenames are the uuid of the call true or false if a leg files are prefixed "a_"'))
    #encode = models.BooleanField(_(u'Encode'), default=True, help_text=_(u'encode the post data may be true for url encoding, false for no encoding or base64 for base64 encoding'))
    lighttpd =  models.BooleanField(_(u'Lighttpd'),default=True, help_text=_(u'optional: set to true to disable Expect: 100-continue lighttpd requires this setting'))
    err_log =  models.CharField(_(u'Error Log DIR'), max_length=240, blank=True, default="log/xml_cdr", help_text=_(u'optional: full path to the error log dir for failed web posts if not specified its the same as log-dir, either an absolute path, a relative path assuming ${prefix}/logs or a blank or omitted value will default to ${prefix}/logs/xml_cdr'))
    cdr_ca =  models.BooleanField(_(u'Disable CA'), default=True, help_text=_(u'optional: if enabled this will disable CA root certificate checks by libcurl note: default value is disabled. only enable if you want this!'))
    enabled = models.BooleanField(_(u'Enable'), default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'cdr_conf'