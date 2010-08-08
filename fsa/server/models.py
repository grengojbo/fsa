# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.dialplan.models import Context, Extension
from fsa.gateway.models import SofiaGateway
from fsa.server.managers import ServerManager
from fsa.acl.models import FSAcl
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
import config
from livesettings import ConfigurationSettings, config_value, config_choice_values
# Create your models here.
VERSION_CHOICES = ( (0, '1.0.5'), (1, '1.0.6'),)
TYPE_CHOICES = ( (0, _(u'SyStem')), (1, _(u'User')),)

class Server(models.Model):
    """
    On a dedicated appliance, there will only be one server
    for the people who bought the appliance.  In other situations
    there might be more than one server.

    Насторйки для управления множеством серверов,
    у вас должно быть как минимум один сервер.
    
    <configuration name="event_socket.conf" description="Socket Client">
      <settings>
        <param name="nat-map" value="false"/>
        <param name="listen-ip" value="127.0.0.1"/>
        <param name="listen-port" value="8021"/>
        <param name="password" value="ClueCon"/>
        <!--<param name="apply-inbound-acl" value="lan"/>-->
      </settings>
    </configuration>
    
    """
    
    name = models.CharField(_(u'Name'), max_length=50)
    listen_ip = models.IPAddressField(_(u'Listen IP'), help_text=_(u'The default settings allow socket connections only from the local host. To allow connections from any host on the network, use 0.0.0.0 instead of the default 127.0.0.1'))
    listen_port = models.PositiveIntegerField(_(u'Listen Port'), help_text=_(u"Is a tcp based interface to control FreeSwitch. Default port listen 8021"))
    listen_acl = models.ForeignKey(FSAcl, verbose_name=_(u'Acl'), default=1, related_name='event_socket', help_text=_(u' Event socet param name="apply-inbound-acl" value="lan"'))
    nat_map = models.BooleanField(_('NAT Map'), default=False)
    password = models.CharField(_(u'Password'), max_length=25)
    sql_name = models.CharField(_(u'SQL Name'), max_length=25, blank=True, null=True, help_text="Name MySQL ODBC Connetion odbc.ini")
    sql_login = models.CharField(_(u'SQL Login'), max_length=25, blank=True)
    sql_password = models.CharField(_(u'SQL Password'), max_length=25, blank=True)
    ssh_user = models.CharField(_(u'SSH User'), max_length=25, blank=True)
    #ssh_password = models.CharField(_(u'SSH Password'), max_length=25, blank=True)
    ssh_host = models.CharField(_(u'SSH Host'), max_length=100, blank=True)
    enabled = models.BooleanField(_(u'Enable'), default=False)
    sites = models.ManyToManyField(Site, related_name='sipsites', blank=True, null=True)
    server_version = models.PositiveSmallIntegerField(_(u'Server Version'), choices=VERSION_CHOICES, default=0)
    acl = models.ManyToManyField(FSAcl, related_name='server_acl')
    objects = ServerManager()

    def __unicode__(self):
        return self.name
    
    @property
    def options(self):
        """Options from confi"""
        return ConfigurationSettings()
            
    @property
    def odbc_dsn(self):
        """string connect ODBC"""
        return "%s:%s:%s" % (self.sql_name, self.sql_login, self.sql_password)
    
    class Meta:
        db_table = 'server'
        verbose_name = _(u'Freeswitch Server')
        verbose_name_plural = _(u'Freeswitch Servers')

class Alias(models.Model):
    name = models.CharField(_(u'Name'), max_length=50, default='default')
    alias_type = models.PositiveSmallIntegerField(_(u'Type'), choices=TYPE_CHOICES, default=0)
    
    class Meta:
        db_table = 'sip_alias'
        verbose_name = _(u'SIP Alias')
        verbose_name_plural = _(u'SIP Alias')
    
    def __unicode__(self):
        return self.name

class Conf(models.Model):
    name = models.CharField(_(u'Name'), max_length=50)
    server = models.ForeignKey(Server, verbose_name=_('FreeSWITCH Server'), default=2, related_name='serverfs')
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
    
    server = models.ForeignKey(Server, verbose_name=_('FreeSWITCH Server'), default=2, related_name='sfs')
    alias = models.ManyToManyField('Alias', blank=True, db_table='alias_many', verbose_name=_(u"Alias"), related_name='relalias')
    gateway = models.ManyToManyField(SofiaGateway, blank=True, db_table='server_gateway', verbose_name=_(u"Gateways"), related_name='relgw')
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
    sites = models.ManyToManyField(Site, related_name='servsites', blank=True, null=True)
    # if set to true, lets anything register
    accept_blind_reg = models.BooleanField(_(u'Accept'), default=False, help_text=_(u'If true, anyone can register to server and will not be challenged for username/password information'))
    #context = 
    #dialplan =
    #gateways = 
    codec_prefs = models.CharField(_(u'Inbound Codec'), max_length=100, default="G729,PCMU,GSM")
    outbound_codec_prefs = models.CharField(_(u'Outbound Codec'), max_length=100, default="G729,PCMU,GSM")
    context = models.ForeignKey(Context, blank=True)
    other_param = models.XMLField(_(u'Other Param'), blank=True)
    no_view_param = models.XMLField(_(u'No View Param'), default='<!-- no view -->')
    comments = models.CharField(_(u'Comments'), max_length=254, blank=True)
    default_profile = models.BooleanField(_(u'Default'),default=False)
    
    class Meta:
        db_table = 'sip_profile'
        unique_together = ('name', 'server')
        verbose_name = _(u'SIP Profile')
        verbose_name_plural = _(u'SIP Profiles')

    def __unicode__(self):
        return self.name
    @property
    def nodes(self):
        return self.alias.select_related('name')
        
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

class CsvBase(models.Model):
    """"""
    name = models.CharField(_('Name'), max_length=100)
    val = models.CharField(_('Value'), max_length=255)
    description = models.CharField(_('Description'), max_length=255)
    
    class Meta:
        db_table = 'CsvBase'
        verbose_name = _(u'Format loads csv file')
        verbose_name_plural = _(u'Format loads csv files')
    
    def __unicode__(self):
        return u''
    
    @models.permalink
    def get_absolute_url(self):
        return ('CsvBase', [self.id])
    
import listeners
listeners.start_listening()
