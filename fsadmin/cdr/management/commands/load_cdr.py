# -*- coding: UTF-8 -*-  
from django.core.management.base import NoArgsCommand
from django.core.management import call_command
from django.core.management.color import no_style
import csv, sys
import os
import gzip
import zipfile
from optparse import make_option
from BeautifulSoup import BeautifulStoneSoup as Soup
import time, datetime
from fsadmin.cdr.models import Cdr, Conf
import urllib

from django.core.management.base import BaseCommand


try:
    import bz2
    has_bz2 = True
except ImportError:
    has_bz2 = False

class Command(BaseCommand):
    help = "Load CDR data."
    args = "/usr/local/freeswitch/log/xml_cdr/"

    def handle(self, fixture_labels, **options):
        from django.db.models import get_apps
        from django.core import serializers
        from django.db import connection, transaction
        from django.conf import settings
        import fsadmin.cdr

        self.style = no_style()

        verbosity = int(options.get('verbosity', 1))
        show_traceback = options.get('traceback', False)

        # commit is a stealth option - it isn't really useful as
        # a command line option, but it can be useful when invoking
        # loaddata from within another script.
        # If commit=True, loaddata will use its own transaction;
        # if commit=False, the data load SQL will become part of
        # the transaction in place when loaddata was invoked.
        commit = options.get('commit', True)

        # Keep a count of the installed objects and fixtures
        fixture_count = 0
        object_count = 0
        models = set()

        humanize = lambda dirname: dirname and "'%s'" % dirname or 'absolute path'

        # Get a cursor (even though we don't need one yet). This has
        # the side effect of initializing the test database (if
        # it isn't already initialized).
        cursor = connection.cursor()
    
        if commit:
            transaction.commit_unless_managed()
            transaction.enter_transaction_management()
            transaction.managed(True)

        class SingleZipReader(zipfile.ZipFile):
            def __init__(self, *args, **kwargs):
                zipfile.ZipFile.__init__(self, *args, **kwargs)
                if settings.DEBUG:
                    assert len(self.namelist()) == 1, "Zip-compressed fixtures must contain only one file."
            def read(self):
                return zipfile.ZipFile.read(self, self.namelist()[0])

        compression_types = {
            None:   file,
            'gz':   gzip.GzipFile,
            'zip':  SingleZipReader
        }
        if has_bz2:
            compression_types['bz2'] = bz2.BZ2File

        #app_fixtures = os.path.join(os.path.dirname(fsadmin.cdr.__file__), 'fixtures')
        #print app_fixtures
        time_format = "%Y-%m-%d %H:%M:%S"
        objects_in_fixture = 0
        for fixture_dir in os.listdir(fixture_labels):
            #if verbosity > 1:
            print "Checking %s for fixtures..." % humanize(fixture_dir)
            label_found = False
            fixture_count += 1
            full_path = os.path.join(fixture_labels, fixture_dir)
            f = open(full_path, 'r')
            xml_cdr = Soup(f)
            f.close()
            try:
                objects_in_fixture += 1
                new_cdr = Cdr(caller_id_name = xml_cdr.cdr.callflow.caller_profile.caller_id_name.string, caller_id_number = xml_cdr.cdr.callflow.caller_profile.caller_id_number.string)
                new_cdr.accountcode = xml_cdr.cdr.variables.accountcode.string
                new_cdr.destination_number = xml_cdr.cdr.callflow.caller_profile.destination_number.string
                new_cdr.context = xml_cdr.cdr.callflow.caller_profile.context.string
                new_cdr.start_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.start_stamp.string), time_format)))
                #new_cdr.start_timestamp = '2009-02-24 16:47:54.099098'
                new_cdr.answer_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.answer_stamp.string), time_format)))
                new_cdr.end_timestamp = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(urllib.unquote(xml_cdr.cdr.variables.end_stamp.string), time_format)))
                new_cdr.duration = xml_cdr.cdr.variables.duration.string
                new_cdr.billsec = xml_cdr.cdr.variables.billsec.string
                new_cdr.hangup_cause = xml_cdr.cdr.variables.hangup_cause.string
                new_cdr.uuid = xml_cdr.cdr.callflow.caller_profile.uuid.string
                new_cdr.read_codec = xml_cdr.cdr.variables.read_codec.string
                new_cdr.write_codec = xml_cdr.cdr.variables.write_codec.string
                #print xml_cdr.cdr.variables.answer_stamp.string
                new_cdr.save()
                object_count += objects_in_fixture
                label_found = True
            except Exception:
                import traceback
                transaction.rollback()
                transaction.leave_transaction_management()
                if show_traceback:
                    traceback.print_exc()
                else:
                    sys.stderr.write(self.style.ERROR("Problem installing fixture '%s': %s\n" %
                                    (full_path, ''.join(traceback.format_exception(sys.exc_type, 
                                    sys.exc_value, sys.exc_traceback))))) 
                return
            
            # If the fixture we loaded contains 0 objects, assume that an
            # error was encountered during fixture loading.
            if objects_in_fixture == 0:
                sys.stderr.write(self.style.ERROR("No fixture data found for '%s'. (File format may be invalid.)" % (fixture_name)))
                transaction.rollback()
                transaction.leave_transaction_management()
                return

        #filename = "tmp/lcr.csv"
        #reader = csv.reader(open(filename, "rb"), delimiter=';')
        #try:
        #    for row in reader:
        #        print row
        #    except csv.Error, e:
        #       sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        #call_command('loaddata', 'alias.xml', 'server.xml', 'sipprofile.xml', 'fsgroup.xml', 'context.xml', interactive=True)
        
        # If we found even one object in a fixture, we need to reset the
        # database sequences.
        if object_count > 0:
            sequence_sql = connection.ops.sequence_reset_sql(self.style, models)
            if sequence_sql:
                if verbosity > 1:
                    print "Resetting sequences"
                for line in sequence_sql:
                    cursor.execute(line)

        if commit:
            transaction.commit()
            transaction.leave_transaction_management()

        if object_count == 0:
            if verbosity > 1:
                print "No fixtures found."
        else:
            if verbosity > 0:
                print "Installed %d object(s) from %d fixture(s)" % (object_count, fixture_count)

        # Close the DB connection. This is required as a workaround for an
        # edge case in MySQL: if the same connection is used to
        # create tables, load data, and query, the query can return
        # incorrect results. See Django #7572, MySQL #37735.
        if commit:
            connection.close()
