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
from fsa.core.utils import pars_phone

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
    def read(self, request, start=0, limit=50, phone=None, si=None):
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
            if phone is not None and si is not None:
                log.info(phone)
                #SELECT l.digits AS digits, cg.name AS gw, l.rate AS rate, cg.prefix AS gw_prefix, cg.suffix AS suffix, l.price AS price, l.price_currency AS currency, l.name AS name, l.lead_strip, l.trail_strip, l.prefix, l.suffix FROM lcr l LEFT JOIN carrier_gateway cg ON l.carrier_id_id=cg.id LEFT JOIN django_site s ON l.site_id=s.id WHERE cg.enabled = '1' AND l.enabled = '1' AND l.digits IN (380442, 380) AND CURRENT_TIMESTAMP BETWEEN l.date_start AND l.date_end AND CURTIME() BETWEEN l.time_start AND l.time_end AND (DAYOFWEEK(NOW()) = l.weeks OR l.weeks = 0) AND s.name="089.com.ua" ORDER BY  digits DESC, reliability DESC, quality DESC;
                #, rand();
                #select DAYOFWEEK(NOW()) IN (weeks);
                query = "SELECT l.digits AS digits, cg.name AS gw, l.rate AS rate, cg.prefix AS gw_prefix, cg.suffix AS suffix, l.price AS price, l.price_currency AS currency, l.name AS name FROM lcr l LEFT JOIN carrier_gateway cg ON l.carrier_id_id=cg.id LEFT JOIN django_site s ON l.site_id=s.id WHERE cg.enabled = '1' AND l.enabled = '1' AND l.digits IN (%s) AND CURRENT_TIMESTAMP BETWEEN l.date_start AND l.date_end AND CURTIME() BETWEEN l.time_start AND l.time_end AND (DAYOFWEEK(NOW()) = l.weeks OR l.weeks = 0) AND s.name='%s' ORDER BY  digits DESC, reliability DESC, quality DESC;" % (pars_phone(phone), si)
                resp = base.raw(query)[0]
                return {"rate": resp.rate, "suffix": resp.suffix, "digits": resp.digits, "gw": resp.gw, "price": resp.price, "currency": resp.currency, "name": resp.name }
            else:
                resp = base.filter(tariff_plan__id=tariff, enabled=True, tariff_plan__site__name__exact=request.user)[start:limit]
                count = base.filter(tariff_plan__id=tariff, enabled=True, tariff_plan__site__name__exact=request.user).count()
                return {"count": count, "lcr": resp}
        except:
            return rc.NOT_HERE
        #try:
            #if phone is not None:
                #server = ServerProxy("http://%s:%s@%s:%s" % (config_value('SERVER', 'rcpuser'), config_value('SERVER', 'rcppasswd'), config_value('SERVER', 'rcphost'), config_value('SERVER', 'rcpport')))
                #log.debug('connect to server: %s' % config_value('SERVER', 'rcpuser'))
                #qphone = "%s default as xml" % phone
                #resp = server.freeswitch.api("lcr", qphone)
                #xml_resp = Soup(resp)
                #return {"count": 1, "rate": xml_resp.row.rate.string}
            #else:
                #resp = base.filter(site__name__iexact=request.user)[start:limit]
                #count = base.filter(site__name__iexact=request.user).count()
                #return {"count": count, "lcr": resp}
        #except:
            #return rc.NOT_HERE

