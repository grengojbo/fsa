# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import re, os, shutil

#from .managers import 

__author__ = '$Author: $'
__revision__ = '$Revision: $'


# Create your models here.
BREAK = (
   ("on-false","on-false"),
   ("on-true","on-true"),
   ("always","always"),
   ("never","never"),
)
        
class Extension(models.Model):
    """
    An extension, the equivalent of the file-based extensions in
    default_context.xml:

    <extension name="neoconf">
      <condition field="destination_number" expression="^neoconf[-]?([0-9]*)$">
        <action application="set" data="conf_code=$1"/>
        <action application="python" data="neoconf.ivr.prompt_pin"/>
      </condition>
    </extension>
    
    """
    name = models.CharField(_(u'Name'), max_length=50, unique=True)
    continue_on = models.BooleanField(_(u'Continue ON'), default=False)
    #context = models.ForeignKey(Context)
    #pref = models.IntegerField()
    #auth_call = models.BooleanField(_(u'Dialplan Security'), default=True, help_text='experimenting with dialplan security')
    dest_num = models.CharField(_(u'Destination Number'), max_length=75, default='^neoconf[-]?([0-9]*)$', help_text='a regex expression that will be used to match against the destination number (number called by endpoint) eg: ^neoconf[-]?([0-9]*)$')
    desc = models.CharField(_(u'Description'), max_length=250, default='welcome message')

    # the actions in a malformed rootless xml snippet:
    # <action application="set" data="conf_code=$1"/>
    # <action application="python" data="neoconf.ivr.prompt_pin"/>
    # yes, this assumes only basic usage, but in fact _anything_
    # stuck in here will be mirrored into the dialplan result
    # returned from views.xml_dialplan()
    actions_xml = models.XMLField(u'Actions', default='', help_text='the actions in a malformed rootless xml snippet: <action application="set" data="conf_code=$1"/>')
    is_temporary = models.BooleanField(u'Temporary', default=False, help_text='is this a temporary extension?')
    is_condition = models.BooleanField(u'Is condition', default=False, help_text='No build condition?')
    enabled = models.BooleanField(_(u'Enable'), default=False)
    # is this extension associated w/ a particular endpoint?
    # eg, when user creates them both at the same time
    #endpoint = models.ForeignKey("Endpoint", null=True)

    # the priority position of this extension, relative to other extensions.
    # think of the list of extensions as if they were in a a file
    # so the "top" extension corresponds to priority position 0,
    # the one below to 1, etc.  nothing fancy here, just a simple ordering.
    priority_position = models.IntegerField(_(u'Priority position'), default=0, help_text='the "top" extension corresponds to priority position 0, the one below to 1, etc.  nothing fancy here, just a simple ordering.')

    @property
    def dest_num_matches(self, destnum2test):
        groups = re.findall(self.dest_num, destnum2test)
        return groups

    @property
    def actions_xml_dom(self):
        """
        get a dom object like
        <actions_xml>
        <action application="set" data="conf_code=$1"/>
        <action application="python" data="neoconf.ivr.prompt_pin"/>        
        </actions_xml>
        where everything inside <actions_xml> comes right out
        of the actions_xml field
        """
        #xml_text = "<actions_xml>%s</actions_xml>" % self.actions_xml
        #dom = minidom.parseString(xml_text)
        #return dom
        pass

    @property
    def xml_preview(self):
        """
        get the first X chars of xml for preview purposs
        """
        numchars = 50
        retval = "Error"

        # chop off repetitive head if found
        # <action application="speak" data="cepstral|William.. -->
        # <...="speak" data="cepstral|William.. -->
        retval = re.sub(r'action application', r'...', self.actions_xml)

        if len(retval) > numchars:
            retval = "%s.." % retval[:numchars]
        return retval
    
    @property
    def sofia_url(self):
        """
        get the dialable url for this extension, eg,
        sofia/mydomain.com/600@ip:port
        """
        # single_expansion = self.get_single_expansion()
        # if not single_expansion:
        #     raise Exception("There is no single expansion for this "
        #                     "extension: %s" % str(self))
        # return sofiautil.extension_url(single_expansion, self.account)
        pass
                                       
    @property    
    def single_expansion(self):
        """
        does the destination number for this extension have
        a singl expansion?  
        ^600$ -> 600
        ^\d+$ -> None
        """
        # find what's inside the ^()$, eg, ^600$ -> 600.  600->600
        # optional ^ specified by \^?, followed by any number of
        # anything except $ specified by ([^\$]*), followed
        # by optional $ specified by \$?
        regex = "\^?([^\$]*)\$?"
        groups = re.findall(regex, self.dest_num)
        stuffinside = groups[0]

        # at this point, group will be something like "600", or if
        # self.dest_num is empty, will be an empty string
        # now, find out if its alphanum ONLY, eg, no regex
        # specifiers.  do this by "regexing it against itself".
        # things like 600 will match, whereas things like 
        # '60(2|3)0' will fail.  and things like *98 will blow up *boom*
        try:
            groups = re.findall(stuffinside, stuffinside) 
            if groups:
                # doesnt cover every case, for example..
                # 1?4085400303
                if groups[0] == stuffinside:
                    return stuffinside
                else:
                    return None
            else:
                return None
        except:
            # this will happen in the case of an illegal regex, such as *98  
            return None

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'dialplan_extension'
        verbose_name = _(u'Dialplan Extension')
        verbose_name_plural = _(u'Dialplan Extensions')

class Context(models.Model):
    # TODO перенести default_context в настройки для сайта
    name = models.CharField(_(u'Name'), max_length=50, unique=True)
    default_context = models.BooleanField(_(u'Default'),default=False)
    extension = models.ManyToManyField(Extension, blank=True, null=True, related_name='exten')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'dialplan_context'
        verbose_name = _(u'Dialplan Context')
        verbose_name_plural = _(u'Dialplan Contexts')
        
#class Condition(m.Model):
#    field = m.CharField(max_length=255)
#    expression = m.CharField(max_length=255)
#    break_on = m.CharField(max_length=10,choices=BREAK,default="on-false")
#    extension = m.ForeignKey(Extension)
#    pref = m.IntegerField()
#    def __unicode__(self):
#        return "%s === %s"%(self.field,self.expression)
#    class Meta:
#        ordering = ['pref']

#class DPApp(m.Model):
#    name = m.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name

#def get_dpapp(app):
#    f = DPApp.objects.filter(name=app)
#    if f:
#        return f[0]
#    else:
#        new = DPApp(name=app)
#        new.save()
#        return new

#class Action(m.Model):
#    app = m.ForeignKey(DPApp)
#    condition = m.ForeignKey(Condition)
#    params = m.CharField(max_length=255)
#    anti = m.BooleanField()
#    pref = m.IntegerField()
#    def __unicode__(self):
#        return "%s(%s)"%(self.app.name,self.params)
#    class Meta:
#        ordering = ['pref']

