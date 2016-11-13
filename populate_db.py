import os, sys
import importlib
import datetime
import urllib, json

from app.models import *
conf = load_config(os.path.join(here, 'config.yaml'))

sqlite_dbs = [conf['databases']['dev']]

for fname in sqlite_dbs:
    try:
        print ("Removing {0}.".format(fname))
        os.remove(fname)
    except OSError:
        pass

for fname in sqlite_dbs:
    if os.path.isfile(fname):
        print ("Database {0} should not exist at this point!".format(fname))
    print("Creating empty SQLite file: {0}".format(fname))
    open(fname, 'a').close()

def class_from_name(module_name, class_name):
    c = getattr(module_name, class_name)
    return c

def get_classes (db):
    classes = []
    for str in conf['models'][db]:
        print ("\tCreating model for '{0}'".format(str))
        c = class_from_name(sys.modules[__name__], str)
        classes.append(c)
    return classes

mainDB.create_tables(get_classes('mainDB'))

url = "https://www.govtrack.us/api/v2/bill?congress=114"
response = urllib.urlopen(url)
data = json.loads(response.read())

for x in data['objects']:
    if x['is_alive']:
        Bill(id                  = x['id'],
             title               = x['title'],
             display_num         = x['display_number'],
             bill_type           = x['bill_type'],
             bill_type_label     = x['bill_type_label'],
             congress            = x['congress'],
             current_status      = x['current_status'],
             current_status_date = x['current_status_date'],
             link_web            = x['link'],
             is_alive            = x['is_alive']).save()
        print("Added the Bill " +x['link'])
