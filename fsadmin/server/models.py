# -*- coding: UTF-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.dialplan.models import Context, Extension
from fsadmin.gateway.models import SofiaGateway
from fsa.server.managers import ServerManager
# Create your models here.
#from django.db import models
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.auth.models import User
#import datetime, re, os, sys, shutil
#from time import strftime
#from pytz import timezone
#from StringIO import StringIO
#from xml.dom import minidom
#from xml.dom.ext import PrettyPrint
#import re

#from wikipbx import logger, utils, sofiautil

class Server(models.Model):
    """
    On a dedicated appliance, there will only be one server
    for the people who bought the appliance.  In other situations
    there might be more than one server.

    Насторйки для управления множеством серверов,
    у вас должно быть как минимум один сервер.
    
    <configuration name="event_socket.conf" description="Socket Client">
      <settings>
        <param name="listen-ip" value="127.0.0.1"/>
        <param name="listen-port" value="8021"/>
        <param name="password" value="ClueCon"/>
      </settings>
    </configuration>
    """
    
    name = models.CharField(_(u'Name'), max_length=50)
    # the absolute path to the directory where the
    # application is installed.  used to find the ivr
    # subdirectory for editing IVR scripts.
    #application_root = models.CharField(maxlength=75)

    # the port the FS listens on 
    #server_port = models.PositiveIntegerField()

    # the internal ip address of the webserver
    # 1. what ip address fs should connect to for xml_cdr posts
    #ip = models.CharField(maxlength=24)

    # fully qualified domain name of webserver,
    # at the time of this writing, only used for links that
    # are sent in voicemail email notifications
    # eg, wikipbx.yourdomain.com
    #fqdn = models.CharField(maxlength=100)

    listen_ip = models.IPAddressField(_(u'Listen IP'), help_text=_(u'The default settings allow socket connections only from the local host. To allow connections from any host on the network, use 0.0.0.0 instead of the default 127.0.0.1'))
    listen_port = models.PositiveIntegerField(_(u'Listen Port'), help_text="Is a tcp based interface to control FreeSwitch. Default port listen 8021")
    password = models.CharField(_(u'Password'), max_length=25)
    sql_name = models.CharField(_(u'SQL Name'), max_length=25, blank=True, null=True, help_text="Name MySQL ODBC Connetion odbc.ini")
    sql_login = models.CharField(_(u'SQL Login'), max_length=25, blank=True)
    sql_password = models.CharField(_(u'SQL Password'), max_length=25, blank=True)
    ssh_user = models.CharField(_(u'SSH User'), max_length=25, blank=True)
    ssh_password = models.CharField(_(u'SSH Password'), max_length=25, blank=True)
    ssh_host = models.CharField(_(u'SSH Host'), max_length=100, blank=True)
    enabled = models.BooleanField(_(u'Enable'), default=False)
    objects = ServerManager()

    #def form_dict(self):
    #    result = {}
    #    result["listen_ip"] = self.listen_ip
    #    result["listen_port"] = self.listen_port
    #    result["password"] = self.password
    #    return result

        
    #def generate_xml_config(self):
    #    dom = minidom.Document()
    #    configuration= dom.createElement("configuration")
    #    configuration.setAttribute("name", "event_socket.conf")
    #    configuration.setAttribute("description", "Socket Client")        
    #    dom.appendChild(configuration)
    #    settings = dom.createElement("settings")
    #    configuration.appendChild(settings)
    #    
    #    # replace each param with db value
    #    params_map = {'listen-ip':str(self.listen_ip),
    #                  'listen-port':str(self.listen_port),
    #                  'password':str(self.password)}

    #    for param_name, param_val in params_map.items():
    #        param = dom.createElement("param")
    #        param.setAttribute("name", param_name)
    #        param.setAttribute("value", param_val)
    #        settings.appendChild(param)

    #    # serialize to xml
    #    sio = StringIO()
    #    PrettyPrint(dom, sio)
    #    return sio.getvalue()
    
    #def form_dict(self):
    #    retval = {}
    #    retval['application_root'] = self.application_root
    #    retval['http_port'] = self.http_port
    #    retval['ip'] = self.ip
    #    retval['fqdn'] = self.fqdn        
    #    return retval
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'server'
        verbose_name = _(u'Freeswitch Server')
        verbose_name_plural = _(u'Freeswitch Servers')

class Alias(models.Model):
    name = models.CharField(_(u'Name'), max_length=50, default='default')

    class Meta:
        db_table = 'sip_alias'
        verbose_name = _(u'SIP Alias')
        verbose_name_plural = _(u'SIP Alias')
    
    def __unicode__(self):
        return self.name

class Conf(models.Model):
    name = models.CharField(_(u'Name'), max_length=50)
    #server = models.ForeignKey(Server)
    enabled = models.BooleanField(_(u'Enable'), default=False)
    xml_conf = models.XMLField(u'XML')

    class Meta:
        db_table = 'server_conf'
        verbose_name = _(u'Configuration file')
        verbose_name_plural = _(u'Configuration files')
        #unique_together = ('name', 'server')
    
    def __unicode__(self):
        return self.name


class SipProfile(models.Model):
    """
     SIP Profiles allow you to define paths to devices or carriers
     that may live inside or outside your network. These paths can be of many
     different types, but must consist of a unique combination of port and IP pairs.
     You could have SIP profiles for your internal network, or multiple profiles
     for each subnet of your internal network, or even completely different protocols
     like IPv6 as profile definitions. This helps FreeSWITCH identify how to route 
     different types of calls when necessary, and also gives you the flexibility
     to tailor your dialplans based on what path a call originates to/from.

     SIP профили позволяют определить путь к устройствам. Эти пути могут быть разных типов,
     но должны состоять из уникального сочетания порта и IP адресса.
     Вы можете иметь SIP профиль для вашей внутренней сети, или несколько профилей 
     для каждой подсети вашей внутренней сети, или даже абсолютно разные протоколы, 
     как IPv6. Это помогает определить, каким образом FreeSWITCH будет маршрутерезировать пути
     для разных типов вызовов, когда это необходимо, а также дает возможность
     адаптировать ваши план набора.
    """
    # this will be the sofia profile name.  perhaps this field
    # should be merged with name.
    # Имя sofia профиля
    name = models.CharField(_(u'Name'), max_length=50, default='internal')
    
    server = models.ForeignKey(u'Server')
    alias = models.ManyToManyField('Alias', blank=True, db_table='alias_many')
    gateway = models.ManyToManyField(SofiaGateway, blank=True, db_table='server_gateway')
    #admins = models.ManyToManyField('UserProfile',related_name="admins")
    enabled = models.BooleanField(_(u'Enable'), default=True)
    proxy_media  = models.BooleanField(_(u'Proxy Media'), default=False)

    ext_rtp_ip = models.CharField(_(u'External RTP IP'), max_length=50, blank=True, help_text=_(u"Use the external/public IP address of the machine. If you are behind NAT, you can use the internal IP but you won't be able to use endpoints or interconnect with machines outside your LAN. If your ip changes and you use dynamic dns you can try entering the domain name (not well tested) OR you can enter stun:stun.freeswitch.org."))
    ext_sip_ip = models.CharField(_(u'External SIP IP'), max_length=50, blank=True, help_text=_(u'See comments on External RTP IP'))

    # will be returned with directory xml: <domain name="$${domain}">
    # for all endpoints that belong to this account.
    # all sip endpoints for this account MUST use this domain when
    # connecting to the switch.  when endpoints are dialed,
    # this domain is used: eg, sofia/foo/100%foo.com.  perhaps
    # this field should be merged with domain.
    # if left blank, the system falls back to ext_sip_ip.
    domain = models.CharField(_(u'Domain'), max_length=50, blank=True, help_text=_(u'(Optional) the domain that sip endpoints for this account will register to. If left blank, endpoints should register to the IP given in External SIP IP'))
    rtp_ip = models.IPAddressField(_(u'RTP IP'))
    sip_ip = models.IPAddressField(_(u'SIP IP'))
    sip_port = models.PositiveIntegerField(_(u'SIP port'), default=5060)
    
    # if set to true, lets anything register
    accept_blind_reg = models.BooleanField(_(u'Accept'), default=False, help_text=_(u'If true, anyone can register to server and will not be challenged for username/password information'))
    #context = 
    #dialplan =
    #gateways = 
    codec_prefs = models.CharField(_(u'Codec'), max_length=100, default="G729,PCMU,GSM")
    context = models.ForeignKey(Context, blank=True)
    other_param = models.XMLField(_(u'Other Param'), blank=True)
    comments = models.CharField(_(u'Comments'), max_length=254, blank=True)

    class Meta:
        db_table = 'sip_profile'
        unique_together = ('name', 'server')
        verbose_name = _(u'SIP Profile')
        verbose_name_plural = _(u'SIP Profiles')

    def __unicode__(self):
        return self.name

    def get_domain(self):
        # return domain, or ext_sip_ip if no domain set
        if self.domain:
            return self.domain
        else:
            return self.ext_sip_ip

    def short_name(self):
        numchars = 10
        if len(self.name) <= numchars:
            return self.name
        else:
            return "%s.." % self.name[:8]



    
