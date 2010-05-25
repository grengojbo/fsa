# -*- mode: python; coding: utf-8; -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.handler import PaginatedCollectionBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsa.numberplan.api.handlers')
from fsa.numberplan.models import NumberPlan

class NumberPlanHandler(PaginatedCollectionBaseHandler):
    #class NumberPlanHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    #allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = NumberPlan
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('phone', 'nt', 'enables', 'status', 'date_active')
    #resources = NumberPlan.objects.filter(site__name__exact=request.user)
    
    #@staticmethod
    #def resource_uri(cls, numberplan):
        #return ('numberplan', [ 'json', ])
    
    def read(self, request, phone=None):
        self.resource_name = 'numberplan'
        #return {"count": 0, "numberplan": NumberPlan.objects.filter(site__name__exact=request.user)}
        if phone is not None:
            log.debug("phone: %s" % phone)
            return {"count": 1, 'numberplan': NumberPlan.objects.get(phone_number__exact=phone, site__name__exact=request.user)}
            #self.resources = NumberPlan.objects.filter(site__name__exact=request.user)
        else:
            self.resources = NumberPlan.objects.filter(site__name__exact=request.user)
            return super(NumberPlanHandler, self).read(request)


    def update(self, request, phone):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        log.debug("update phone number %s" % phone)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            try:
                np = NumberPlan.objects.get(phone_number__exact=phone, site__name__exact=request.user)
                np.nt=int(attrs['nt'])
                np.save()
                return np
            except:
                return rc.BAD_REQUEST

    def delete(self, request, phone):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        try:
            np = NumberPlan.objects.get(phone_number__exact=phone, site__name__exact=request.use)
            np.enables=False
            np.save()
            return rc.DELETED
        except:
            return rc.NOT_HERE

