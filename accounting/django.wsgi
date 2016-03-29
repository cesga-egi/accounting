import os
import sys

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
path= '/usr/local/accounting/'
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'accounting.settings'

import django
django.setup()
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
