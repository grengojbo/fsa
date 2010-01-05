# -*- coding: UTF-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# Create your models here.
class VoicemailMsgs(models.Model):
    created_epoch = models.IntegerField(null=True, blank=True)
    read_epoch = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    uuid = models.CharField(max_length=255, blank=True)
    cid_name = models.CharField(max_length=255, blank=True)
    cid_number = models.CharField(max_length=255, blank=True)
    in_folder = models.CharField(max_length=255, blank=True)
    file_path = models.CharField(max_length=255, blank=True)
    message_len = models.IntegerField(null=True, blank=True)
    flags = models.CharField(max_length=255, blank=True)
    read_flags = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'voicemail_msgs'

class VoicemailPrefs(models.Model):
    username = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    name_path = models.CharField(max_length=255, blank=True)
    greeting_path = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'voicemail_prefs'

class DbData(models.Model):
    hostname = models.CharField(max_length=255, blank=True)
    realm = models.CharField(max_length=255, blank=True)
    data_key = models.CharField(max_length=255, blank=True)
    data = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'db_data'

class SipSubscriptions(models.Model):
    proto = models.CharField(max_length=255, blank=True, null=True)
    sip_user = models.CharField(max_length=255, blank=True, null=True)
    sip_host = models.CharField(max_length=255, blank=True, null=True)
    sub_to_user = models.CharField(max_length=255, blank=True, null=True)
    sub_to_host = models.CharField(max_length=255, blank=True, null=True)
    presence_hosts = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=3072, blank=True, null=True)
    call_id = models.CharField(max_length=255, blank=True, null=True)
    full_from = models.CharField(max_length=255, blank=True, null=True)
    full_via = models.CharField(max_length=255, blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    accept = models.CharField(max_length=255, blank=True, null=True)
    profile_name = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    network_ip = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = u'sip_subscriptions'

class SipRegistrations(models.Model):
    call_id = models.CharField(max_length=255, blank=True)
    sip_user = models.CharField(max_length=255, blank=True)
    sip_host = models.CharField(max_length=255, blank=True)
    presence_hosts = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=3072, blank=True)
    status = models.CharField(max_length=255, blank=True)
    rpid = models.CharField(max_length=255, blank=True)
    expires = models.IntegerField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    server_user = models.CharField(max_length=255, blank=True)
    server_host = models.CharField(max_length=255, blank=True)
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    network_ip = models.CharField(max_length=255, blank=True)
    network_port = models.CharField(max_length=18, blank=True)
    sip_username = models.CharField(max_length=255, blank=True)
    sip_realm = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'sip_registrations'

class SipSharedAppearanceDialogs(models.Model):
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    contact_str = models.CharField(max_length=255, blank=True)
    call_id = models.CharField(max_length=255, blank=True)
    expires = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sip_shared_appearance_dialogs'

class SipSharedAppearanceSubscriptions(models.Model):
    subscriber = models.CharField(max_length=255, blank=True)
    call_id = models.CharField(max_length=255, blank=True)
    aor = models.CharField(max_length=255, blank=True)
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    contact_str = models.CharField(max_length=255, blank=True)
    network_ip = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'sip_shared_appearance_subscriptions'

class SipDialogs(models.Model):
    call_id = models.CharField(max_length=255, blank=True)
    uuid = models.CharField(max_length=255, blank=True)
    sip_to_user = models.CharField(max_length=255, blank=True)
    sip_to_host = models.CharField(max_length=255, blank=True)
    sip_from_user = models.CharField(max_length=255, blank=True)
    sip_from_host = models.CharField(max_length=255, blank=True)
    contact_user = models.CharField(max_length=255, blank=True)
    contact_host = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    direction = models.CharField(max_length=255, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'sip_dialogs'

class SipPresence(models.Model):
    sip_user = models.CharField(max_length=255, blank=True)
    sip_host = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    rpid = models.CharField(max_length=255, blank=True)
    expires = models.IntegerField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    network_ip = models.CharField(max_length=255, blank=True)
    network_port = models.CharField(max_length=18, blank=True)
    class Meta:
        db_table = u'sip_presence'
        
class SipAuthentication(models.Model):
    nonce = models.CharField(max_length=255, blank=True)
    expires = models.IntegerField(null=True, blank=True)
    profile_name = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'sip_authentication'

class LimitData(models.Model):
    hostname = models.CharField(max_length=255, blank=True)
    realm = models.CharField(max_length=255, blank=True)
    uuid = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'limit_data'

# class SipAlias(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'sip_alias'
