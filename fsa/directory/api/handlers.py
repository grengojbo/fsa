# -*- mode: python; coding: utf-8; -*- 
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
#from piston.doc import generate_doc
import logging
log = logging.getLogger('fsb.directory.api.handlers')
from fsa.directory.models import Endpoint

class EndpointHandler(BaseHandler):
    """
    Authenticated entrypoint for blogposts.
    """
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Endpoint
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('uid', 'phone_type', 'password', 'accountcode', 'effective_caller_id_name','enable', 'is_registered', 'last_registered', 'description')
    
    #@staticmethod
    #def resource_uri():
    #    return ('api_numberplan_handler', ['phone_number'])
    #@require_mime('json', 'yaml')
    def read(self, request, start=0, limit=5, phone_number=None, account=None):
        """
        Returns a blogpost, if `title` is given,
        otherwise all the posts.

        Parameters:
         - `phone_number`: The title of the post to retrieve.
        """
        log.debug("read endpoint % s" % account)
        base = Endpoint.objects
        #accountcode=account
        if phone_number:
            return {"count": 1, "accounts": base.get(uid=phone_number)}
        else:
            return {"count": 1000, "accounts": base.all()[start:limit]}

    def update(self, request, phone_number):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            np = Balance.objects.get(accountcode=phone_number)
            np.nt=attrs['nt']
            np.save()

            return np

    def delete(self, request, phone_number):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)

        np = Balance.objects.get(accountcode=phone_number)
        np.enables=False
        np.save()

        return np

    def create(self, request):
        """
        Update number plan type.
        """
        attrs = self.flatten_dict(request.POST)

        np = Balance.objects.get(accountcode=account)
        np.enables=False
        np.save()

        return np
