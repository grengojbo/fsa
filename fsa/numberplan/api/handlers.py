# -*- mode: python; coding: utf-8; -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsa.numberplan.api.handlers')
from fsa.numberplan.models import NumberPlan

class NumberPlanHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    #allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = NumberPlan
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('phone_number', 'nt', 'enables', 'status', 'date_active')

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
        if request.GET.get("start"):
            start = request.GET.get("start")
        if request.GET.get("limit"):
            limit = int(request.GET.get("limit"))
            limit += int(start)
        log.info(limit)
        try:
            if phone_number:
                return {"count": 1, "phonenumber": base.get(phone_number=phone_number, site__name__iexact=request.user)}
            else:
                resp = base.filter(site__name__iexact=request.user)[start:limit]
                count = base.filter(site__name__iexact=request.user).count()
                return {"count": count, "phonenumber": resp}
        except:
            return rc.NOT_HERE

    def update(self, request, phone_number):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            try:
                np = NumberPlan.objects.get(phone_number=phone_number, site__name__iexact=request.user)
                np.nt=attrs['nt']
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
            np = NumberPlan.objects.get(phone_number=phone_number, site__name__iexact=request.use)
            np.enables=False
            np.save()
            return rc.DELETED
        except:
            return rc.NOT_HERE

