# -*- mode: python; coding: utf-8; -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.handler import PaginatedCollectionBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsa.directory.api.handlers')
from fsa.directory.models import Endpoint
from fsa.server.models import SipProfile
import keyedcache
from fsa.numberplan.models import NumberPlan
from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.db import transaction

class EndpointHandler(PaginatedCollectionBaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Endpoint
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('uid', 'password', 'username', 'effective_caller_id_name','enable', 'is_registered', 'last_registered', 'description', 'sip_server', 'reg_server')

    #@require_mime('json', 'yaml')
    def read(self, request, phone=None, account=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        log.debug("read endpoint %s" % account)
        #base = Endpoint.objects
        self.resource_name = 'phone'
        try:
            if phone is not None:
                return {"count": 1, "phone": Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)}
            elif account is not None:
                self.resources = Endpoint.objects.filter(accountcode__username__exact=account, site__name__exact=request.user)
                return super(EndpointHandler, self).read(request)
            else:
                self.resources = Endpoint.objects.filter(site__name__exact=request.user)
                return super(EndpointHandler, self).read(request)
        except:
            return rc.NOT_HERE

    @transaction.commit_on_success
    def update(self, request, phone):
        """
        Update number plan type.
        """
        try:
            attrs = self.flatten_dict(request.POST)
            #if self.exists(**attrs):
            #return rc.DUPLICATE_ENTRY
            #else:
            endpoint = Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)
            if attrs.get('effective_caller_id_name'):
                endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
            if attrs.get('password'):
                endpoint.password = attrs.get('password')
            if attrs.get('description'):
                endpoint.description = attrs.get('description')
            if attrs.get("enabled") == "false":
                endpoint.enable = False
            elif attrs.get("enabled") == "true":
                endpoint.enable = True
            if attrs.get("enable") == "false":
                endpoint.enable = False
            elif attrs.get("enable") == "true":
                endpoint.enable = True
            endpoint.save()
            return endpoint
        except:
            return rc.NOT_HERE

    @transaction.commit_on_success
    def delete(self, request, phone):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        try:
            endpoint = Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)
            np = NumberPlan.objects.get(phone_number=phone, site__name__exact=request.user)
            endpoint.enable=False
            np.status=2
            endpoint.save()
            np.save()
            # TODO add parking
            return rc.DELETED
        except:
            return rc.NOT_HERE

    @transaction.commit_on_success
    def create(self, request):
        try:
            attrs = self.flatten_dict(request.POST)
            u = User.objects.get(username__exact=attrs.get('username'))
            s = Site.objects.get(name__exact=request.user)
            if attrs.get('phone'):
                np = NumberPlan.objects.get(phone_number__exact=attrs.get('phone'), site__name__exact=request.user, status=0)
                if np.phone_number == attrs.get('phone'):
                    endpoint = Endpoint.objects.create_endpoint(user=u, phone_number=attrs.get('phone'), site=s)
                else:
                    return rc.NOT_HERE
            else:
                endpoint = Endpoint.objects.create_endpoint(user=u, site=s)
            if attrs.get('effective_caller_id_name'):
                endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
            else:
                endpoint.effective_caller_id_name = "%s %s" % (u.first_name, u.last_name)
            if attrs.get("enabled") == "false":
                endpoint.enable = False
            elif attrs.get("enabled") == "true":
                endpoint.enable = True
            if attrs.get("enable") == "false":
                endpoint.enable = False
            elif attrs.get("enable") == "true":
                endpoint.enable = True
            if attrs.get('password'):
                endpoint.password = attrs.get('password')
            if attrs.get('description'):
                endpoint.description = attrs.get('description')
            log.debug(endpoint)
            endpoint.site = s
            endpoint.save()
            #resp = rc.ALL_OK
            #resp = rc.CREATED
            #resp.write(endpoint)
            #return resp
            return endpoint
        except:
            resp = rc.DUPLICATE_ENTRY
            return resp

class DirectorytHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST',)

    def read(self, request, phone=None, account=None):
        return {"count": 2}

    #require_mime('xml')
    def create(self, request):
        attrs = self.flatten_dict(request.POST)
	    #log.debug(request.POST)
        key_value = name = 'result'
        xml_context = '<result status="not found" />'
        user = request.user
        if user.has_perm("billing.api_view"):
            if attrs.get('section') == "directory":
                #if attrs.get('action') and attrs.get('action') == 'message-count':
                    #key_caches_endpoint = "endpoint::{0}".format(attrs.get('user'))
                    #key_extra_context = "endpoint::context::{0}".format(attrs.get('user'))
                    #try:
                        #extra_context = keyedcache.cache_get(key_extra_context)
                    #except:
                        #try:
                            #endpoint = Endpoint.objects.get(uid__exact=attrs.get('user'), enable=True)
                            #extra_context = {'template': 'directory/sip_reg.xml', 'extra_context': {'name':name, 'context':endpoint.context, 'account':endpoint.accountcode.pk, 'tariff':endpoint.tariff, 'key_value':"view::endpoint::{0}".format(attrs.get('user')), 'sip':endpoint, 'domain':attrs.get('domain')}}
                            #keyedcache.cache_set(key_caches_endpoint, value=endpoint)
                            #keyedcache.cache_set(key_extra_context, value=extra_context)
                        #except:
                            #endpoint = None
                            #extra_context = {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':"view::endpoint::{0}".format(attrs.get('user')), 'xml_context':xml_context}}
                            #keyedcache.cache_set(key_caches_endpoint, value=endpoint)
                            #keyedcache.cache_set(key_extra_context, value=extra_context)
                    #return extra_context
                if attrs.get('profile') and attrs.get('purpose') == 'gateways':
                    key_caches = "directory::gw::sites::{0}".format(attrs.get('profile'))
                    try:
                        sites = keyedcache.cache_get(key_caches)
                        return {'template': 'directory/gw.xml', 'extra_context': {'sc': sites.count(), 'sites': sites}}
                    except keyedcache.NotCachedError, nce:
                        try:
                            sofia = SipProfile.objects.get(enabled=True, name__exact=attrs.get('profile'))
                            sites = sofia.sites.all().values()
                            keyedcache.cache_set(key_caches, value=sites)
                            return {'template': 'directory/gw.xml', 'extra_context': {'sc': sites.count(), 'sites': sites}}
                        except:
                            #keyedcache.cache_set(key_caches, value=None)
                            keyedcache.cache_delete(key_caches)
                            return {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':key_value, 'xml_context':xml_context}}
                elif attrs.get('purpose') == 'network-list':
                    key_caches = "directory:::network-list:::{0}".format(attrs.get('hostname'))
                    return {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':key_value, 'xml_context':xml_context}}
                elif attrs.get('user') and attrs.get('domain'):
                    #elif attrs.get('action') and attrs.get('action') == 'sip_auth':
                    key_caches_endpoint = "endpoint::{0}".format(attrs.get('user'))
                    key_extra_context = "endpoint::context::{0}".format(attrs.get('user'))
                    try:
                        extra_context = keyedcache.cache_get(key_extra_context)
                    except:
                        try:
                            endpoint = Endpoint.objects.get(uid__exact=attrs.get('user'), enable=True)
                            #endpoint = Endpoint.objects.get(uid__exact=attrs.get('user'), enable=True, sip_profile__name__exact=attrs.get('sip_profile'))
                            extra_context = {'template': 'directory/sip_reg.xml', 'extra_context': {'name':name, 'sitename':endpoint.sitename, 'context':endpoint.context, 'account':endpoint.accountcode.pk, 'tariff':endpoint.tariff, 'site_id':endpoint.site.pk, 'key_value':"view::endpoint::{0}".format(attrs.get('user')), 'sip':endpoint, 'domain':attrs.get('domain')}}
                            keyedcache.cache_set(key_caches_endpoint, value=endpoint)
                            keyedcache.cache_set(key_extra_context, value=extra_context)
                        except:
                            endpoint = None
                            extra_context = {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':"view::endpoint::{0}".format(attrs.get('user')), 'xml_context':xml_context}}
                            keyedcache.cache_set(key_caches_endpoint, value=endpoint)
                            keyedcache.cache_set(key_extra_context, value=extra_context)
                            log.error("NO_PHOHE Directory API post domain: {0}, user: {1}".format(attrs.get('user'), attrs.get('domain')))
                    log.debug("Directory API post domain: {0}, user: {1}".format(attrs.get('user'), attrs.get('domain')))
                    return extra_context
                else:
                    return {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':key_value, 'xml_context':xml_context}}
            else:
                return {'template': 'server/fs.xml', 'extra_context': {'name':name, 'key_value':key_value, 'xml_context':xml_context}}
        else:
            return rc.FORBIDDEN

