# -*- mode: python; coding: utf-8; -*- 
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsa.directory.api.handlers')
#from fsa.directory.models import Endpoint
#from fsa.numberplan.models import NumberPlan
from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.db import transaction
from fsa.lcr.models import Lcr
from xmlrpclib import ServerProxy
from livesettings import ConfigurationSettings, config_value
from BeautifulSoup import BeautifulStoneSoup as Soup

class LcrHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET')
    model = Lcr
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('digits', 'name', 'country_code', 'rate', 'weeks', 'time_start', 'time_end')

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
        base = Lcr.objects
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

