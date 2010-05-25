# -*- mode: python; coding: utf-8; -*- 
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.handler import PaginatedCollectionBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsb.directory.api.handlers')
from fsa.directory.models import Endpoint
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

    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, phone=None, account=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        log.debug("read endpoint %s" % account)
        base = Endpoint.objects
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
        #attrs = self.flatten_dict(request.POST)
        #endpoint = Endpoint.objects.get(uid__exact=phone, site__name__exact=request.user)
        #if attrs.get('effective_caller_id_name'):
            #endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
        #if attrs.get('password'):
            #endpoint.password = attrs.get('password')
        #if attrs.get('description'):
            #endpoint.description = attrs.get('description')
        #if attrs.get("enabled") == "false":
            #endpoint.enable = False
        #elif attrs.get("enabled") == "true":
            #endpoint.enable = True
        #if attrs.get("enable") == "false":
            #endpoint.enable = False
        #elif attrs.get("enable") == "true":
            #endpoint.enable = True
        #endpoint.save()
        #return endpoint
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
        #attrs = self.flatten_dict(request.POST)
        #u = User.objects.get(username__exact=attrs.get('username'))
        #s = Site.objects.get(name__exact=request.user)
        #log.debug(u)
        #if attrs.get('phone'):
            #np = NumberPlan.objects.get(phone_number__exact=attrs.get('phone'), site__name__exact=request.user, status=0)
            #if np.phone_number == attrs.get('phone'):
                #endpoint = Endpoint.objects.create_endpoint(user=u, phone_number=attrs.get('phone'), site=s)
            #else:
                #return rc.NOT_HERE
        #else:
            #endpoint = Endpoint.objects.create_endpoint(user=u, site=s)
        #log.debug(endpoint)
        #return endpoint
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

