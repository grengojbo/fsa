# -*- mode: python; coding: utf-8; -*-
from piston.handler import BaseHandler
import logging
from django.contrib.auth.models import User

l = logging.getLogger('fsa.api.handler')
class FreeSwitchAdminHandler(BaseHandler):
   allowed_methods = ('POST',)
   model = User
   fields = ('username',)
   def create(self, request):
       pass
       
   def read(self, request, title=None):
       return User.objects.get(user=request.user)