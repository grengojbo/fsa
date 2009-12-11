# -*- coding: UTF-8 -*-
from django import test
from django.core import mail
from django.contrib.auth.models import User

#from lib.helpers import reverse
from fsa.core import appcheck    
from fsa.core import is_app

class CoreTestCase(test.TestCase):
    fixtures = ['context', 'extension', 'alias', 'server', 'acl', 'gateway', 'fsgroup', 'sipprofile', 'testnp', 'testenpoint']
    def setUp(self):
        self.name = 'megatest'
        #self.email = 'something@example.com'
        #self.user = ActionRecord.registrations.create_inactive_user(name=self.name, email=self.email, password=self.name)
        #self.em = mail.outbox[0]
        #self.ar = self.user.actionrecord_set.get(type='A')

    def testAppcheck(self):
        tr = 0
        if is_app('fsa.core'):
            tr = 1
        self.assertEqual(tr, 1)
        tr = 0
        if is_app('fsadmin.nax'):
            tr = 1
        self.assertEqual(tr, 0)

    


