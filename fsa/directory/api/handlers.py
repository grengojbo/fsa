# -*- mode: python; coding: utf-8; -*- 
from piston.handler import BaseHandler, AnonymousBaseHandler
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

class EndpointHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Endpoint
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('uid', 'password', 'accountcode', 'effective_caller_id_name','enable', 'is_registered', 'last_registered', 'description')
    
    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, start=0, limit=5, phone=None, account=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        log.debug("read endpoint % s" % account)
        base = Endpoint.objects
        #accountcode=account
        if phone is not None:
            return {"count": 1, "phone": base.get(uid=phone, site__name__iexact=request.user)}
        elif account is not None:
            resp = base.filter(accountcode__username__iexact=account, site__name__iexact=request.user)[start:limit]
            count = base.filter(accountcode__username__iexact=account, site__name__iexact=request.user).count()
            return {"count": count, "phone": resp}
        else:
            resp = base.filter(site__name__iexact=request.user)[start:limit]
            count = base.filter(site__name__iexact=request.user).count()
            return {"count": count, "phone": resp}

    @transaction.commit_on_success
    def update(self, request, phone):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        try:
            if self.exists(**attrs):
                return rc.DUPLICATE_ENTRY
            else:
                np = NumberPlan.objects.get(phone_number=attrs.get('phone'), site__name__iexact=request.user)
                endpoint = Endpoint.objects.create_endpoint(u, attrs.get('phone'), site__name__iexact=request.user)
                if attrs.get('effective_caller_id_name'):
                    endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
                if attrs.get('password'):
                    endpoint.password = attrs.get('password')
                if attrs.get('description'):
                    endpoint.description = attrs.get('description')
                return np
        except:
            return rc.BAD_REQUEST

    @transaction.commit_on_success
    def delete(self, request, phone):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        try:
            endpoint = Endpoint.objects.get(uid=phone, site__name__iexact=request.user)
            endpoint.enable=False
            endpoint.save()
            return rc.DELETED
        except:
            return rc.NOT_HERE

    @transaction.commit_on_success
    def create(self, request):
        attrs = self.flatten_dict(request.POST)
        u = User.objects.get(username=attrs.get('account'))
        s = Site.objects.get(name=request.user)
        try:
            if attrs.get('phone'):
                np = NumberPlan.objects.get(phone_number=attrs.get('phone'), site__name__iexact=request.user, enables=False, status=0)
                if np.phone_number == attrs.get('phone'):
                    endpoint = Endpoint.objects.create_endpoint(u, attrs.get('phone'))
                else:
                    return rc.NOT_HERE
            else:
                np = NumberPlan.objects.lphonenumber(s)
                endpoint = Endpoint.objects.create_endpoint(u, attrs.get('phone'))
            if attrs.get('effective_caller_id_name'):
                endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
            if attrs.get("enabled") == "false":
                endpoint.enable = False
            if attrs.get('password'):
                endpoint.password = attrs.get('password')
            if attrs.get('description'):
                endpoint.description = attrs.get('description')
            endpoint.site = s
            endpoint.save()
            resp = rc.CREATED
            #resp.write(endpoint)
            return resp
        except:
            resp = rc.DUPLICATE_ENTRY
            return resp

