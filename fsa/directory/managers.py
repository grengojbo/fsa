# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from django.template import Context, loader
from django.contrib.auth.models import User
from fsa.dialplan.models import Context
from fsa.server.models import SipProfile
#from fsa.numberplan.models import NumberPlan
#from fsa.directory.models import Endpoint as e
from django.conf import settings
from django.db.models import Avg, Max, Min, Count
import logging
import datetime

l = logging.getLogger('fsa.directory.managers')

class EndpointManager(models.Manager):
    """
    """
    # TODO: add endpoint is not number plan
    # DoesNotExist
    # Exception Value: NumberPlan matching query does not exist.
    def lactive(self):
        """
        return -- только активные шлюзы
        """
        return self.filter(enable=True)
    
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

    def gen_password(self, limlen=10):
        """
        """
        pass

    def new_endpoint(self):
        pass
    
    def create_endpoint(self, user, phone_number=None, site=None):
        """
        Added new endpoint
        
        Keyword arguments:  
        user -- User
        phone_number -- Phone Number default: None
        
        """
        from fsa.numberplan.models import NumberPlan
        
        n = self.model()
        if phone_number is None:
            n.uid = NumberPlan.objects.lphonenumber(site)
        else:
            n.uid = phone_number
        n.password = User.objects.make_random_password(10, "0123456789")
        n.accountcode = user
        # TODO: добавить значение по умолчанию
        n.user_context = Context.objects.get(default_context=True)
        n.sip_profile =  SipProfile.objects.get(default_profile=True)
        n.effective_caller_id_name = user.username
        n.enable = True
        n.phone_type = 'S'
        n.save()
        NumberPlan.objects.lactivate(n.uid)
        l.debug("create endpoint: %s" % n.uid)
        return n
        #try:
            #n.password = User.objects.make_random_password(6, "0123456789")
            #n.accountcode = user
            ## TODO: добавить значение по умолчанию
            #n.user_context = Context.objects.get(default_context=True)
            #n.sip_profile =  SipProfile.objects.get(default_profile=True)
            #n.effective_caller_id_name = user.username
            #n.enable = True
            #n.phone_type = 'S'
            #n.save()
            #NumberPlan.objects.lactivate(n.uid)
            #l.debug("create endpoint: %s" % n.uid)
            #return n
        #except DoesNotExist:
            #raise 
            #return None

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
