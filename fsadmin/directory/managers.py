# -*- coding: UTF-8 -*-
from django.db import models
#from django.template import Context, loader
from django.contrib.auth.models import User
from fsa.dialplan.models import Context
from fsa.server.models import SipProfile
#from fsa.numberplan.models import NumberPlan
#from fsadmin.directory.models import Endpoint as e
from django.conf import settings
from django.db.models import Avg, Max, Min, Count
import logging
import datetime

l = logging.getLogger('fsadmin.directory.managers')

class EndpointManager(models.Manager):
    """
    """
    def get_next_number(self):
        """
        return - Next free Endpoints Number
        """
        r = self.aggregate(Max('uid'))
        if (r['uid__max']):
            #l.debug(r)
            return r['uid__max'] + 1
        else:
            return settings.START_PHONE_NUMBER

    def gen_password(self, limlen=6):
        """
        """
        pass

    def create_endpoint(self, user):
        """
        Добавляем новый номер
        """
        from fsa.numberplan.models import NumberPlan
        
        n = self.model()
        n.uid = NumberPlan.objects.set_number()
        n.password = User.objects.make_random_password(6, "0123456789")
        n.accountcode = user
        # TODO: добавить значение по умолчанию
        n.user_context = Context.objects.all()[0]
        n.sip_profile =  SipProfile.objects.all()[0]
        #Context.objects.filter(default_context=True).values()[0]
        n.effective_caller_id_name = user.username
        n.enable = True
        n.phone_type = 'S'
        n.save()
        l.debug(n.uid)
        return n

    def reg(self):
        n = self.model()
        n.is_registered = True
        n.last_registered = datetime.now
        n.save()



class SipRegistrationManager(models.Manager):
    def sip_auth_nc(self, p, u):
        """
        return 0 ошибка при добавлении такой sip уже есть при удалении не такого sip
               1 зарегистрировался sip
               2 отсоеденился sip
        """   
        # TODO при регистрации изменяем запись в таблице endpoint 
        #if p.get('sip_auth_nc') == '00000001' or p.get('sip_auth_nc') == '00000002':
        try:
            l.debug('sip registration')
            n = self.model()
            n.domain= p.get('domain')
            n.user = u
            n.ip = p.get('ip')
            n.sip_auth_username = p.get('sip_auth_username')
            n.sip_auth_method = p.get('sip_auth_method')
            n.sip_auth_nonce = p.get('sip_auth_nonce')
            n.sip_auth_qop = p.get('sip_auth_qop')
            n.sip_auth_realm = p.get('sip_auth_realm')
            n.sip_auth_uri = p.get('sip_auth_uri')
            n.sip_auth_cnonce = p.get('sip_auth_cnonce')
            n.sip_auth_response = p.get('sip_auth_response')
            n.sip_user_agent = p.get('sip_user_agent')
            n.sip_from_user = p.get('sip_from_user')
            n.sip_from_host = p.get('sip_from_host')
            n.sip_to_user = p.get('sip_to_user')
            n.sip_to_host = p.get('sip_to_host')
            n.sip_contact_user = p.get('sip_contact_user')
            n.sip_contact_host = p.get('sip_contact_host')
            n.sip_request_host = p.get('sip_request_host')
            if p.get('sip_auth_nc') == '00000002':
                n.save()  
            # TODO unregister ->  p.get('sip_auth_nc') == '00000004'
            return 1
        except:
            l.debug('ERROR sip registration')
            return 0
        #else:
        #    try:
        #        s = self.get(sip_auth_nonce = p.get('sip_auth_nonce'))
        #        s.delete()
        #        return 2
        #    except:
        #        return 0
