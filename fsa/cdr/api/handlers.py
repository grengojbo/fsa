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

log = logging.getLogger('fsa.cdr.api.handlers')

class CdrHandler(BaseHandler):

    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST')
    model = Cdr
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('accountcode', 'caller_id_name', 'caller_id_number', 'destination_number', 'context', 'start_timestamp', 'answer_timestamp', 'end_timestamp', 'duration', 'billsec', 'hangup_cause', 'uuid')

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
        attrs = self.flatten_dict(request.POST)
        log.debug(attrs.get('cdr'))
        resp = rc.CREATED
        #resp.write(endpoint)
        return resp
##        attrs = self.flatten_dict(request.POST)
##        u = User.objects.get(username=attrs.get('account'))
##        s = Site.objects.get(name=request.user)
##        try:
##            if attrs.get('phone'):
##                np = NumberPlan.objects.get(phone_number=attrs.get('phone'), site__name__iexact=request.user, enables=False, status=0)
##                if np.phone_number == attrs.get('phone'):
##                    endpoint = Endpoint.objects.create_endpoint(u, attrs.get('phone'))
##                else:
##                    return rc.NOT_HERE
##            else:
##                np = NumberPlan.objects.lphonenumber(s)
##                endpoint = Endpoint.objects.create_endpoint(u, attrs.get('phone'))
##            if attrs.get('effective_caller_id_name'):
##                endpoint.effective_caller_id_name = attrs.get('effective_caller_id_name')
##            if attrs.get("enabled") == "false":
##                endpoint.enable = False
##            if attrs.get('password'):
##                endpoint.password = attrs.get('password')
##            if attrs.get('description'):
##                endpoint.description = attrs.get('description')
##            endpoint.site = s
##            endpoint.save()
##            resp = rc.CREATED
##            #resp.write(endpoint)
##            return resp
##        except:
##            resp = rc.DUPLICATE_ENTRY
##            return resp