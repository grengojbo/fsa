# -*- mode: python; coding: utf-8; -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.handler import PaginatedCollectionBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsa.numberplan.api.handlers')
from fsa.numberplan.models import NumberPlan

class NumberPlanHandler(PaginatedCollectionBaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    #allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = NumberPlan
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('phone', 'nt', 'enables', 'status', 'date_active')

    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, start=0, limit=50, phone_number=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        log.debug("read phone number %s" % phone_number)
        base = NumberPlan.objects
        try:
            if phone_number:
                #return {"count": 1, "phonenumber": base.get(phone_number__exact=phone_number, site__name__exact=request.user)}
                resp = base.get(phone_number__exact=phone_number, site__name__exact=request.user)
            else:
                resp = base.filter(site__name__exact=request.user)
                #count = base.filter(site__name__exact=request.user).count()
                #return {"count": count, "phonenumber": resp}
            return resp
        except:
            return rc.NOT_HERE

    def update(self, request, phone_number):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        log.debug("update phone number %s" % phone_number)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            try:
                np = NumberPlan.objects.get(phone_number__exact=phone_number, site__name__exact=request.user)
                np.nt=int(attrs['nt'])
                np.save()
                return np
            except:
                return rc.BAD_REQUEST

    def delete(self, request, phone_number):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)
        try:
            np = NumberPlan.objects.get(phone_number__exact=phone_number, site__name__exact=request.use)
            np.enables=False
            np.save()
            return rc.DELETED
        except:
            return rc.NOT_HERE

